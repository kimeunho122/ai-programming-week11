import pytest

from ai_B import read_grades


def write_csv(tmp_path, contents):
	path = tmp_path / "grades.csv"
	path.write_text(contents, encoding="utf-8")
	return path


def test_reads_valid_rows_and_score_boundaries(tmp_path):
	path = write_csv(tmp_path, "name,score\nAlice,0\nBob,100\n")

	valid, skipped = read_grades(path)

	assert valid == [("Alice", 0), ("Bob", 100)]
	assert skipped == []


@pytest.mark.parametrize(
	"row",
	[
		",80",       # empty name
		"Alice,",     # empty score
		"Bob,abc",    # non-integer score
		"Carol,-1",   # below range
		"Dave,101",   # above range
		"Eve",        # too few columns
		"Frank,80,x", # too many columns
	],
)
def test_invalid_rows_are_skipped_and_recorded(tmp_path, row):
	path = write_csv(tmp_path, f"name,score\n{row}\n")

	valid, skipped = read_grades(path)

	assert valid == []
	assert len(skipped) == 1
	assert skipped[0]


@pytest.mark.parametrize("contents", ["", "name,score\n"])
def test_empty_or_header_only_file_returns_empty_results(tmp_path, contents):
	path = write_csv(tmp_path, contents)

	valid, skipped = read_grades(path)

	assert valid == []
	assert skipped == []


def test_missing_file_raises_file_not_found_error(tmp_path):
	with pytest.raises(FileNotFoundError):
		read_grades(tmp_path / "missing.csv")


def test_unreadable_path_raises_os_error(tmp_path):
	# A directory cannot be read as a CSV file.
	with pytest.raises(OSError):
		read_grades(tmp_path)
