#!/usr/bin/env python3
"""
YOLO 이미지 객체 탐지 스크립트
"""

import cv2
from ultralytics import YOLO
import os
import argparse

def detect_objects_in_image(image_path, output_path=None, model_name='yolov8n.pt'):
    """
    이미지에서 객체 탐지 수행
    
    Args:
        image_path (str): 입력 이미지 경로
        output_path (str): 출력 이미지 경로 (None이면 화면에 표시)
        model_name (str): 사용할 YOLO 모델 이름
    """
    
    print(f"이미지 객체 탐지 시작: {image_path}")
    
    # YOLO 모델 로드
    model = YOLO(model_name)
    
    # 이미지 읽기
    image = cv2.imread(image_path)
    if image is None:
        print(f"❌ 이미지를 읽을 수 없습니다: {image_path}")
        return
    
    # 객체 탐지 수행
    results = model(image)
    
    # 결과 분석
    if results[0].boxes is not None:
        num_objects = len(results[0].boxes)
        print(f"✅ 감지된 객체 수: {num_objects}")
        
        # 각 객체 정보 출력
        for i, box in enumerate(results[0].boxes):
            class_id = int(box.cls)
            confidence = float(box.conf)
            class_name = model.names[class_id]
            print(f"  객체 {i+1}: {class_name} (신뢰도: {confidence:.2f})")
    else:
        print("감지된 객체가 없습니다.")
    
    # 결과를 이미지에 그리기
    annotated_image = results[0].plot()
    
    # 출력 처리
    if output_path:
        cv2.imwrite(output_path, annotated_image)
        print(f"결과 이미지 저장: {output_path}")
    else:
        # 화면에 표시
        cv2.imshow('YOLO Detection Result', annotated_image)
        print("아무 키나 눌러서 창을 닫으세요.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser(description='YOLO 이미지 객체 탐지')
    parser.add_argument('image_path', help='입력 이미지 경로')
    parser.add_argument('-o', '--output', help='출력 이미지 경로')
    parser.add_argument('-m', '--model', default='yolov8n.pt', 
                       choices=['yolov8n.pt', 'yolov8s.pt', 'yolov8m.pt', 'yolov8l.pt', 'yolov8x.pt'],
                       help='사용할 YOLO 모델')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.image_path):
        print(f"❌ 이미지 파일이 존재하지 않습니다: {args.image_path}")
        return
    
    detect_objects_in_image(args.image_path, args.output, args.model)

if __name__ == "__main__":
    # 명령행 인수가 없으면 예제 실행
    import sys
    if len(sys.argv) == 1:
        print("사용법:")
        print("  python yolo_image_detection.py <이미지_경로> [-o 출력_경로] [-m 모델명]")
        print("\n예제:")
        print("  python yolo_image_detection.py test.jpg")
        print("  python yolo_image_detection.py test.jpg -o result.jpg -m yolov8s.pt")
    else:
        main()