# 원티드 프리온보딩 백엔드 인턴십 선발과제
## 프로젝트 환경
- Python : 3.10
- Django : 4.2.6
- djangorestframework : 3.14.0
- SQLite

## 요구사항
### 채용공고 등록
- url : `recuritment/`
- 회사는 아래와 같이 채용 공고를 등록한다.
```
{
    "id": 1,
    "company_name": "회사A",
    "nation": "한국",
    "region": "서울",
    "position": "백엔드개발자",
    "compensation": 1000000,
    "tech": "python"
}
```
### 채용공고 수정
- url : `recuritment/update/<int:pk>/`
### 채용공고 삭제
- url : `recuritment/delete/<int:pk>/`
### 채용공고 목록 조회
- url : `recuritment/list/`
- 사용자는 아래와 같이 채용공고 목록을 확인할 수 있다.
```
[
    {
        "id": 1,
        "company_name": "회사A",
        "nation": "한국",
        "region": "서울",
        "position": "백엔드개발자",
        "compensation": 1000000,
        "tech": "python"
    },
    {
        "id": 4,
        "company_name": "회사A",
        "nation": "한국",
        "region": "서울",
        "position": "프론트엔드 개발자",
        "compensation": 500000,
        "tech": "React"
    },
    {
        "id": 5,
        "company_name": "회사B",
        "nation": "한국",
        "region": "경기",
        "position": "백엔드개발자",
        "compensation": 1000000,
        "tech": "Java"
    }
]
```
### 채용공고 검색 기능
- url : `recuritment/list/?search=<검색키워드>`
- 회사명, 채용포지션, 사용기술 키워드로 검색할 수 있도록 구현

### 채용공고 상세 페이지 조회
- url : `recuritment/<int:pk>/`
- 채용 내용이 추가적으로 담겨있음
- 해당 회사가 올린 다른 채용 공고가 추가적으로 포함
    - `serializers.SerializerMethodField()`를 활용하여 구현함
```
{
    "id": 5,
    "company_name": "회사B",
    "nation": "한국",
    "region": "경기",
    "position": "백엔드개발자",
    "compensation": 1000000,
    "tech": "Java",
    "contents": "지원바람",
    "recuritments": [6]
}
```
### 사용자는 채용공고에 지원할 수 있다.
- url : `recuritment/apply/`
- 사용자는 1회만 지원 가능
- 요청 받은 사용자의 지원 내역이 있는지 확인하고 없는 경우에만 지원할 수 있도록 구현
