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

The device control is provided by the 2x16 LCD screen and 6 buttons on the device. Raspberry Pi Zero Wireless was used as a development board in order to enable the device to perform all desired functions. As the operating system, Raspberry Pi OS, a Linux-based operating system, was used and the control software was written in Python language. Some scripts used are written with Bash Script.

The card is powered by a 5V 3A adapter. The STD MTR QK1-4640 24V 9000 RPM DC motor, which will enable the surface to be coated to rotate, was chosen arbitrarily in line with the available facilities and was provided free of charge. L298 motor driver circuit, which will drive the engine, can take in enough speed and it is the most affordable driver circuit solding in Turkey. The motor and driver circuit are powered by a 19V 3.42A Adapter and provide the required power for the desired performance. The speed of the engine is measured with the LM393 integrated infrared speed sensor circuit, and a control system is used to keep the engine speed constant at the desired speed by using the signals received from the sensor. Plastic junction box with dimensions of 210mm x 280mm x 138.5mm was preferred for the outer casing of the device in terms of its flexible structure and strength. The disc which the surface to be coated will sit, the parts that will hold the surface and the disc that will be used to count the engine speed are produced by 3D printing. For the transparent inner wall and outer cover for protection purposes, the plastic transparent bowl and plastic pot, which are easily available from the market, were cut and used in appropriate sizes.

The device is ready for use approximately 27 seconds after it is turned on. During this period, the necessary software is run. Up to 10 stages can be defined while programming the device. The device can reach the desired speed within an average of 5 seconds and keep it constant with an average of 6% margin of error. This error can go down to 2% at high speeds.

The device has been tested with a transparent PVC coating of 2mm thickness and 2x2 cm dimensions. Nail polish diluted with acetone was used as coating material.

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


### Circuit Diagram

<img width="300" src="https://user-images.githubusercontent.com/54535282/103857549-c7754f00-50c7-11eb-8797-557379ded70a.png">

