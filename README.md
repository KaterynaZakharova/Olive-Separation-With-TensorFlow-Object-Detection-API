# Olive-Separation-With-TensorFlow-Object-Detection-API


The steps:


### 1. Make 75 photos.
(25 black olives, 25 green olives, 25 both)

**Examples of images:**
![image_example_1](image_example_1.jpg)
![image_example_2](image_example_2.jpg)
![image_example_3](image_example_3.jpg)

### 2. Transform images into a size of 300x300.
Using *transform_image_resolution.py*

### 3. Create annotations in LableImg.
Creating CSV format from XML using *xml_to_csv.py*

### 4. Generate TFRecords.
Using *generate_tfrecord.py*

### 5. Create a label map file and a configuration file.

### 6. Train model.

### 7. Export the inference graph.

### 8. Test the model.
**Input:**
![frame0](frame0.jpg)
![frame70](frame70.jpg)

**Output:**
