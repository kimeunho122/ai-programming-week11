import csv

import pytest

from ai_A import load_scores


def write_csv(tmp_path, rows, *, bom=False):
	path = tmp_path / "scores.csv"
	with path.open("w", encoding="utf-8-sig" if bom else "utf-8", newline="") as file:
		csv.writer(file).writerows(rows)
	return path


def test_load_scores_keeps_valid_rows_and_inclusive_boundaries(tmp_path):
	path = write_csv(
		tmp_path,
		[["name", "score"], [" Alice ", "0"], ["Bob", "100"], ["Cara", "42"]],
		bom=True,
	)

	assert load_scores(path) == ([
		("Alice", 0),
		("Bob", 100),
		("Cara", 42),
	], [])


@pytest.mark.parametrize(
	("row", "reason"),
	[
		(["Too", "many", "columns"], "열 개수가 2가 아님"),
		(["Only one"], "열 개수가 2가 아님"),
		(["   ", "50"], "이름이 비어 있음"),
		(["No score", "  "], "점수가 비어 있음"),
		(["Not integer", "3.5"], "점수가 정수가 아님"),
		(["Negative", "-1"], "점수가 0~100 밖"),
		(["Over", "101"], "점수가 0~100 밖"),
	],
)
def test_load_scores_records_invalid_rows(tmp_path, row, reason):
	path = write_csv(tmp_path, [["name", "score"], row])

	assert load_scores(path) == ([], [(2, ",".join(row), reason)])


def test_load_scores_ignores_header_and_empty_rows(tmp_path):
	path = tmp_path / "scores.csv"
	path.write_text("name,score\n\nValid,75\n", encoding="utf-8")

	assert load_scores(path) == ([ ("Valid", 75) ], [])


def test_load_scores_missing_file_raises(tmp_path):
	with pytest.raises(FileNotFoundError):
		load_scores(tmp_path / "missing.csv")
