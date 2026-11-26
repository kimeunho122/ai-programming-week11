# (프로그램 이름을 적으세요)

<!--
  README 여섯 칸 빈 양식입니다.
  이 파일의 이름을 README.md 로 바꾸고, 아래 여섯 칸을 채우세요.
  <!-- 로 시작하는 줄은 설명이므로 다 채운 뒤 지우면 됩니다.

  판정 기준 — 처음 보는 사람이 3분 안에 실행할 수 있는가.
  마지막에 짝이 실제로 해 봅니다.
-->

## ① 무엇을 하나요 (What)

성적 CSV 파일을 읽어 유효한 점수와 건너뛴 행 기록을 반환합니다.



## ② 왜 만들었나요 (Why)          ★ AI는 이 칸을 못 씁니다

<!--
  코드만 보고는 알 수 없는 칸입니다.
  어떤 문제가 있었고, 그래서 무엇이 필요했는지 두세 문장으로 적으세요.
  예) 실제 파일에는 빈 칸 · 범위 밖 점수 · 중복 이름이 섞여 있어
      그냥 읽으면 프로그램이 죽기 때문입니다.
-->실제 CSV에 빈 칸·범위 밖 점수·중복이나 잘못된 형식이 섞여 있어 오류가 나거나 잘못 집계될 수 있습니다. 유효한 데이터만 걸러 내고 문제 행은 건너뛰며 기록하려고 만들었습니다.  



## ③ 어떻게 쓰나요 (How)

<!-- 설치와 실행 명령을 그대로 복사해 붙일 수 있게. 직접 실행해 보고 적으세요. -->

```bash
# 설치
pip install pytest
# 실행
python -c "from load_scores import load_scores; print(load_scores('scores.csv'))"
```

## ④ 어떻게 테스트하나요

<!-- pytest 실행 방법과, 통과했을 때 나오는 화면을 붙여 넣으세요. -->pytest -v

```bash

```
PS C:\Users\mccoi\OneDrive\문서\GitHub\ai-programming-week11> import pytest
>> from load_scores import load_scores
>> 
>> 
>> def test_없는_파일이면_오류가_난다():
>>   with pytest.raises(FileNotFoundError):
>>     load_scores("없는파일.csv")
>> 
>> 
>> def test_헤더만_있으면_빈_결과가_나온다():
>>   with open("임시_헤더.csv", "w", encoding="utf-8") as f:
>>     f.write("name,score\n")
>>   kept, skipped = load_scores("임시_헤더.csv")
>>   assert kept == []
>>   assert skipped == []
>> 
>> 
>> def 쓰기(파일명, 점수):
>>   with open(파일명, "w", encoding="utf-8") as f:
>>     f.write(f"name,score\n홍길동,{점수}\n")
>> 
>> 
>> @pytest.mark.parametrize(
>>     "점수, 유효한가",
>>     [
>>         (-1, False),  # 경계 바로 아래
>>         (0, True),  # ★ 아래쪽 경계
>>         (1, True),
>>         (99, True),
>>         (100, True),  # ★ 위쪽 경계
>>         (101, False),  # 경계 바로 위
>>     ],
>> )
>> def test_점수_경계값(점수, 유효한가):
>>   쓰기("임시.csv", 점수)
>>   kept, skipped = load_scores("임시.csv")
>>   assert (len(kept) == 1) == 유효한가
PS C:\Users\mccoi\OneDrive\문서\GitHub\ai-programming-week11> python -m pytest -v week11_files\week11_files\test_load_scores.py
================================================================================================================== test session starts ==================================================================================================================
platform win32 -- Python 3.14.7, pytest-9.2.0, pluggy-1.7.0 -- C:\Users\mccoi\AppData\Local\Python\pythoncore-3.14-64\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\mccoi\OneDrive\문서\GitHub\ai-programming-week11
plugins: cov-7.1.0
collected 8 items                                                                                                                                                                                                                                        

week11_files/week11_files/test_load_scores.py::test_없는_파일이면_오류가_난다 PASSED                                                                                                                                                               [ 12%]
week11_files/week11_files/test_load_scores.py::test_헤더만_있으면_빈_결과가_나온다 PASSED                                                                                                                                                          [ 25%]
week11_files/week11_files/test_load_scores.py::test_점수_경계값[-1-False] PASSED                                                                                                                                                                   [ 37%]
week11_files/week11_files/test_load_scores.py::test_점수_경계값[0-True] PASSED                                                                                                                                                                     [ 50%]
week11_files/week11_files/test_load_scores.py::test_점수_경계값[1-True] PASSED                                                                                                                                                                     [ 62%]
week11_files/week11_files/test_load_scores.py::test_점수_경계값[99-True] PASSED                                                                                                                                                                    [ 75%]
week11_files/week11_files/test_load_scores.py::test_점수_경계값[100-True] PASSED                                                                                                                                                                   [ 87%]
week11_files/week11_files/test_load_scores.py::test_점수_경계값[101-False] PASSED                                                                                                                                                                  [100%]

=================================================================================================================== 8 passed in 0.06s ===================================================================================================================
```
(통과 화면을 여기에 붙여 넣으세요)
```

## ⑤ 파일 구성

<!-- 어떤 파일이 무엇을 하는지 한 줄씩. -->

| 파일 | 하는 일 |
| --- | --- |
| `load_scores.py` | 성적 CSV 파일을 읽어 유효한 점수 목록과 건너뛴 행 기록을 반환합니다. |
| `test_load_scores.py` | 정상·예외·경계값 케이스에 대한 `pytest` 단위 테스트를 수행합니다. |
| `README.md` | 프로그램 개요, 실행 및 테스트 방법, 파일 구성과 작성 정보를 안내합니다. |

## ⑥ 만든 사람 · AI를 어디에 썼는지

<!--
  이름 · 학번, 그리고 AI를 어느 부분에 썼고 무엇을 직접 판단했는지 적으세요.
  커밋 메시지에 넣은 Assisted-by: 줄과 내용이 맞아야 합니다.
-->

- 만든 사람 : 김은호
- AI를 쓴 곳 : `load_scores.py` 로직·검증 기준 정리, `test_load_scores.py` 테스트 케이스 작성, `README.md` 초안 구성
- 내가 직접 판단한 것 : 경계값과 예외 처리 기준 확인, `test_load_scores.py` 테스트 보완, 저장소 파일 위치와 `docs` 커밋 정리

## 라이선스

<!-- 저장소를 만들 때 고른 라이선스를 적으세요. 없으면 아무도 이 코드를 쓸 수 없습니다. -->

MIT License (LICENSE 파일 참고)

