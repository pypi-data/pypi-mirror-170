# MedicalImage

## Build 환경
* `medical-image` 프로젝트 권한이 있는 `pypi` 계정 필요 (김화평 팀장에게 문의)
* `dc-xr-03` 띄울 때 경로에 맞춰 volumes에 `- ../../medical-image:/medical-image` 추가
* 동일 버전 업로드는 오류가 남! 반드시 버전 업 후 업로드 해야 함!

## Build
```
docker exec -it dc-xr-03 /bin/bash
cd /medical-image
./build.sh
```
* `typing-extensions` 관련 Error는 무시

## medical_image를 사용하는 이미지 빌드
* `pypi`에 업로드 후 바로 다운로드는 안 되고, 2~3분 후 다운로드 가능!
