from test import test


def predict(image):
    label, value, image_bbox = test(
        image=image,
        model_dir='liveness_detection/resources/anti_spoof_models',
        device_id=0
    )
