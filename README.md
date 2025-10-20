# YOLO 객체 탐지 개발환경

Python과 YOLO 모델을 사용한 객체 탐지 프로그램 개발을 위한 기본 환경이 구축되었습니다.

## 🎯 설치 완료 사항

### 1. 가상환경
- **환경명**: `yolo_env`
- **Python 버전**: 3.9.23
- **위치**: `C:\Users\ASUS\anaconda3\envs\yolo_env`

### 2. 설치된 패키지
- `ultralytics` (8.3.217) - YOLOv8 구현체
- `opencv-python` (4.12.0.88) - 컴퓨터 비전 라이브러리
- `torch` (2.8.0) - PyTorch 딥러닝 프레임워크
- `torchvision` (0.23.0) - 컴퓨터 비전용 PyTorch 확장
- `matplotlib` (3.9.4) - 그래프 및 시각화
- `numpy` (2.0.2) - 수치 계산
- `pillow` (11.3.0) - 이미지 처리

## 📁 생성된 파일들

### 1. `yolo_detection_test.py`
- 기본 YOLO 객체 탐지 테스트 스크립트
- 웹캠 실시간 탐지 또는 테스트 이미지 처리
- 모델 정보 확인 기능

### 2. `yolo_image_detection.py`
- 이미지 파일 객체 탐지 스크립트
- 명령행 인터페이스 지원
- 다양한 YOLO 모델 선택 가능

### 3. `requirements.txt`
- 필요한 패키지 목록
- 다른 환경에서 쉽게 복제 가능

## 🚀 사용 방법

### 가상환경 활성화
```bash
conda activate yolo_env
```

### 1. 기본 테스트 실행
```bash
python yolo_detection_test.py
```

### 2. 이미지 파일 객체 탐지
```bash
# 기본 사용법
python yolo_image_detection.py image.jpg

# 결과 저장
python yolo_image_detection.py image.jpg -o result.jpg

# 다른 모델 사용
python yolo_image_detection.py image.jpg -m yolov8s.pt
```

### 3. 직접 YOLO 사용
```bash
# YOLO CLI 사용
yolo detect predict model=yolov8n.pt source=image.jpg

# Python 코드에서 사용
python -c "from ultralytics import YOLO; model = YOLO('yolov8n.pt'); model.predict('image.jpg')"
```

## 🔧 모델 정보

### 사용 가능한 YOLOv8 모델
- `yolov8n.pt` - Nano (가장 빠름, 가장 작음)
- `yolov8s.pt` - Small
- `yolov8m.pt` - Medium  
- `yolov8l.pt` - Large
- `yolov8x.pt` - Extra Large (가장 정확함, 가장 느림)

### 지원하는 객체 클래스
- **총 80개 클래스** (COCO 데이터셋 기준)
- 사람, 자동차, 동물, 가구, 전자제품 등

## ✅ 테스트 결과

환경 설정이 성공적으로 완료되었습니다:
- ✅ YOLO 모듈 import 성공
- ✅ OpenCV 모듈 import 성공  
- ✅ YOLOv8 모델 로드 성공
- ✅ 80개 클래스 지원 확인

## 📝 다음 단계

이제 다음과 같은 개발을 진행할 수 있습니다:

1. **커스텀 객체 탐지**: 특정 객체를 탐지하도록 모델 커스터마이징
2. **실시간 처리**: 웹캠이나 비디오 파일 실시간 처리
3. **모델 학습**: 자신만의 데이터셋으로 모델 학습
4. **성능 최적화**: 탐지 속도 및 정확도 개선
5. **GUI 개발**: 사용자 친화적인 인터페이스 개발

## 🔍 문제 해결

환경 관련 문제가 발생하면:
1. 가상환경이 활성화되어 있는지 확인
2. 필요한 패키지가 모두 설치되어 있는지 확인: `pip list`
3. CUDA 지원이 필요한 경우 PyTorch CUDA 버전 설치