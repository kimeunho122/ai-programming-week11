import pytest
from load_scores import load_scores


def test_없는_파일이면_오류가_난다():
  with pytest.raises(FileNotFoundError):
    load_scores("없는파일.csv")


def test_헤더만_있으면_빈_결과가_나온다():
  kept, skipped = load_scores("empty.csv")
  assert kept == []
  assert skipped == []


def 쓰기(파일명, 점수):
  with open(파일명, "w", encoding="utf-8") as f:
    f.write(f"name,score\n홍길동,{점수}\n")


@pytest.mark.parametrize(
    "점수, 유효한가",
    [
        (-1, False),  # 경계 바로 아래
        (0, True),  # ★ 아래쪽 경계
        (1, True),
        (99, True),
        (100, True),  # ★ 위쪽 경계
        (101, False),  # 경계 바로 위
    ],
)
def test_점수_경계값(점수, 유효한가):
  쓰기(f"임시.csv", 점수)
  kept, skipped = load_scores("임시.csv")
  assert (len(kept) == 1) == 유효한가