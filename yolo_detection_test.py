#!/usr/bin/env python3
"""
YOLO 객체 탐지 테스트 스크립트
"""

import cv2
from ultralytics import YOLO
import numpy as np

def main():
    """YOLO 모델을 사용한 기본 객체 탐지 테스트"""
    
    print("YOLO 객체 탐지 테스트 시작...")
    
    # YOLOv8 모델 로드 (처음 실행 시 자동으로 다운로드됨)
    print("YOLOv8 모델 로드 중...")
    model = YOLO('yolov8n.pt')  # nano 버전 (가장 빠름)
    
    # 웹캠 설정
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("웹캠을 찾을 수 없습니다. 테스트 이미지를 사용합니다.")
        # 테스트 이미지 생성
        test_image = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
        
        # 모델 테스트
        results = model(test_image)
        
        print("✅ 모델 로드 및 추론 테스트 성공!")
        print(f"감지된 객체 수: {len(results[0].boxes) if results[0].boxes is not None else 0}")
        
        # 결과 표시
        annotated_frame = results[0].plot()
        cv2.imshow('YOLO Test', annotated_frame)
        cv2.waitKey(3000)  # 3초 대기
        cv2.destroyAllWindows()
        
    else:
        print("웹캠이 감지되었습니다. 실시간 객체 탐지를 시작합니다.")
        print("'q' 키를 눌러서 종료하세요.")
        
        while True:
            # 프레임 읽기
            ret, frame = cap.read()
            if not ret:
                print("프레임을 읽을 수 없습니다.")
                break
            
            # YOLO 모델로 객체 탐지
            results = model(frame)
            
            # 결과를 프레임에 그리기
            annotated_frame = results[0].plot()
            
            # 감지된 객체 정보 출력
            if results[0].boxes is not None:
                num_objects = len(results[0].boxes)
                cv2.putText(annotated_frame, f'Objects: {num_objects}', 
                           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # 화면에 표시
            cv2.imshow('YOLO Real-time Detection', annotated_frame)
            
            # 'q' 키로 종료
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
    
    print("YOLO 객체 탐지 테스트 완료!")

def test_model_info():
    """모델 정보 확인"""
    print("\n=== YOLO 모델 정보 ===")
    model = YOLO('yolov8n.pt')
    
    # 클래스 이름 출력
    print(f"지원하는 클래스 수: {len(model.names)}")
    print("클래스 목록:")
    for i, name in model.names.items():
        print(f"  {i}: {name}")

if __name__ == "__main__":
    main()
    test_model_info()