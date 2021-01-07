# Design and Fabrication of a Cost-Effective Spin Coater

## Project Video

[![Cost-Effective Spin Coater Project](http://img.youtube.com/vi/7xUjQFKw6QM/0.jpg)](http://www.youtube.com/watch?v=7xUjQFKw6QM "Project Video")

## About The Project

### Summary

The main objective of this project is design and fabrication of a cost-effective spin coater for depositing thin films.

The originality of this project is that its design and source code are completely free, usable and modifiable, and the production of a spin coater device is substantially inferior to those available in the market.

This project aims that supporting the free software philosophy through the completely free and open- source design having MIT License, making the product accessible to a wider audience than those sold in the market thanks to low cost, and reinforcing the knowledge gained through engineering education with an engineering design project and completing the deficiencies.

### Literature

The spin coating method is a commonly used coating method to obtain uniform thin material films, usually polymers, on the surface of a substrate using the concept of centrifugal force. This method, which is easy to use, safe and inexpensive, is highly preferred for many applications where high quality layers are required such as microcircuit manufacturing, compact discs, magnetic disk coatings, polymer electronic devices.

The cost of commercial rotary coating devices can range from about 600 to 4000 $ In addition to having a high price, commercial rotary coating devices need a specialist for maintenance and repair. Therefore, a low cost and open source rotary coating device is in demand for academic work and student education, with performance similar to a commercial model in the laboratory.

The aim of this study is to design an easily repairable, open source rotary coating device with functions similar to commercial devices, such as being able to rotate up to 7200 RPM for 3600 seconds and be programmable at a cost of less than 65 $, as well as commercial devices. At the same time, it is aimed to support the free software philosophy by sharing the entire project design free of charge under the MIT license.

### Method

It is aimed to provide device control in two ways. The device can be controlled with 2x16 LCD screen and 6 buttons as well as wirelessly controlled by a computer or mobile device. Raspberry Pi Zero Wireless will be used as a development board in order to enable the device to perform all desired functions. As the operating system, a Linux-based operating system that will be compiled specifically for this work will be used in order to reduce the cost by running the device faster and saving storage space at the same time, and the control software will be written in Python language. However, if necessary, different languages ​​can be used. The card will be powered by a 5V 3A adapter. The STD MTR QK1-4640 24V 9000 RPM DC motor, which will ensure the rotation of the surface to be coated, was chosen arbitrarily in line with the facilities available and provided free of charge. Any engine with sufficient specification can be used. L298 Engine, which will drive integrated circuit, the engine can take in enough speed and is the most suitable driver circuit sold in Turkey. The motor and driver circuit will be fed by a 19V 3.42A Adapter and will provide the required power for the desired performance. The speed of the motor will be measured by the LM393 integrated infrared speed sensor circuit. By using the signals received from the infrared sensor, the engine speed will be kept constant at the desired speed with a control system. Plastic junction box with dimensions of 210mm x 280mm x 138.5mm was preferred for the outer casing of the device in terms of its flexible structure and strength. The disc on which the surface to be coated will sit, the parts that will hold the surface and the disc that will be used to count the engine speed will be produced by 3D printing. The transparent inner wall and outer cover for protection will be made of materials that can be found easily and cheaply in the markets.

One of the leading situations that may hinder the progress of the work is the risk of not proper engine and disc balance. Roughness and errors may occur in 3D printer prints. This imbalance may cause an oscillating movement due to an increase in motor speed. In this case, the oscillation movement will cause the motor or other rotating structures to deteriorate after a while. In order to prevent such a problem, the maximum engine speed can be limited to a speed lower than 7200 RPM within the framework of the results obtained by carrying out necessary tests.

Another factor that needs to be reviewed is the low stabilization that can occur at low revs. The motor may or may not turn with a higher margin of error than expected below a certain speed. In such a case, it may be necessary to increase the minimum speed above a certain level.

### References

[1] Bianchi, R., Pansierra, M., Lima, J., Yagura, L., Andrade, A. Faria, R. 2006. “Spin coater based on brushless dc motor of hard disk drivers”, Progress in Organic Coatings, 57, 33-36.

[2] Sadegh-cheri,M.2016. “Design,Fabrication,andOpticalCharacterizationofaLow-Costand Open-Source Spin Coater”, J. Chem. Educ., 96, 1268-1272.

## Images

### Result

<img height="400" src="https://user-images.githubusercontent.com/54535282/103857848-52eee000-50c8-11eb-85b0-5dcb58865fc9.jpeg">

### Appereance

<img width="300" src="https://user-images.githubusercontent.com/54535282/103856508-d0fdb780-50c5-11eb-926c-7b21c8c615c6.jpeg"> <img width="300" src="https://user-images.githubusercontent.com/54535282/103856517-d5c26b80-50c5-11eb-8c55-0aae2315f564.jpeg"> <img width="300" src="https://user-images.githubusercontent.com/54535282/103856529-d9ee8900-50c5-11eb-8ec6-3924be3d7069.jpeg">

### Rotary Part

<img width="300" src="https://user-images.githubusercontent.com/54535282/103856629-03a7b000-50c6-11eb-8c44-b9532e442f41.jpeg">

### Info

<img width="300" src="https://user-images.githubusercontent.com/54535282/103856699-22a64200-50c6-11eb-94cf-0f436f7accb9.jpeg"> <img width="300" src="https://user-images.githubusercontent.com/54535282/103856709-276af600-50c6-11eb-9204-65d3f18f11b8.jpeg"> <img width="300" src="https://user-images.githubusercontent.com/54535282/103856718-2a65e680-50c6-11eb-9ef6-37ddffd903d6.jpeg">

### Main Menu

<img width="300" src="https://user-images.githubusercontent.com/54535282/103856747-3baef300-50c6-11eb-9380-332cf5fd631c.jpeg"> <img width="300" src="https://user-images.githubusercontent.com/54535282/103856758-4073a700-50c6-11eb-8879-610d389a157c.jpeg"> <img width="300" src="https://user-images.githubusercontent.com/54535282/103856764-41a4d400-50c6-11eb-9d21-e5cc4abfc330.jpeg">

### Run Program Menu

<img width="300" src="https://user-images.githubusercontent.com/54535282/103856809-56816780-50c6-11eb-9885-f0f930c373e7.jpeg"> <img width="300" src="https://user-images.githubusercontent.com/54535282/103856821-5aad8500-50c6-11eb-9414-b6fd585b2312.jpeg">

### Quick Programs Menu

<img width="300" src="https://user-images.githubusercontent.com/54535282/103856855-6dc05500-50c6-11eb-9f50-376dd450b368.jpeg"> <img width="300" src="https://user-images.githubusercontent.com/54535282/103856870-72850900-50c6-11eb-8d24-59c40e16a2f1.jpeg"> <img width="300" src="https://user-images.githubusercontent.com/54535282/103856874-744ecc80-50c6-11eb-962d-ab442f010916.jpeg">
<img width="300" src="https://user-images.githubusercontent.com/54535282/103856883-76b12680-50c6-11eb-9c0a-f22531f55811.jpeg"> <img width="300" src="https://user-images.githubusercontent.com/54535282/103856890-79138080-50c6-11eb-893f-26bb6f6314dc.jpeg">

### Set Manual Program Menu

<img width="300" src="https://user-images.githubusercontent.com/54535282/103856937-8e88aa80-50c6-11eb-89ff-90fda98e52fe.jpeg"> <img width="300" src="https://user-images.githubusercontent.com/54535282/103856946-93e5f500-50c6-11eb-96dd-c450fc7982cd.jpeg"> <img width="300" src="https://user-images.githubusercontent.com/54535282/103856949-95afb880-50c6-11eb-8e4f-940898af463f.jpeg">

### Inside the Device

<img width="300" src="https://user-images.githubusercontent.com/54535282/103856992-aceea600-50c6-11eb-9ea5-1d89dcf65c35.jpeg"> <img width="300" src="https://user-images.githubusercontent.com/54535282/103857005-b2e48700-50c6-11eb-9418-2479707d94fd.jpeg">

### Circuit Diagram

<img width="300" src="https://user-images.githubusercontent.com/54535282/103857549-c7754f00-50c7-11eb-8797-557379ded70a.png">

