# Design and Fabrication of a Cost-Effective Spin Coater

## Summary

The main objective of this project is design and fabrication of a cost-effective spin coater for depositing thin films.

The originality of this project is that its design and source code are completely free, usable and modifiable, and the production of a spin coater device is substantially inferior to those available in the market.

This project aims that supporting the free software philosophy through the completely free and open- source design having MIT License, making the product accessible to a wider audience than those sold in the market thanks to low cost, and reinforcing the knowledge gained through engineering education with an engineering design project and completing the deficiencies.

## Subject, Scope and Literature

The spin coating method is a commonly used coating method to obtain uniform thin material films, usually polymers, on the surface of a substrate using the concept of centrifugal force. This method, which is easy to use, safe and inexpensive, is highly preferred for many applications where high quality layers are required such as microcircuit manufacturing, compact discs, magnetic disk coatings, polymer electronic devices [1].

The cost of commercial rotary coating devices can range from about 3000 to 20000 ₺ depending on the number of features. In addition to having a high price, commercial rotary coating devices need a specialist for maintenance and repair. Therefore, a low cost and open source rotary coating device is in demand for academic work and student education, with performance similar to a commercial model in the laboratory [2].

The aim of this study is to design an easily repairable, open source rotary coating device with functions similar to commercial devices, such as being able to rotate up to 7200 RPM for 3600 seconds and be programmable at a cost of less than 500 ₺, as well as commercial devices. At the same time, it is aimed to support the free software philosophy by sharing the entire project design free of charge under the MIT license.

## Method

It is aimed to provide device control in two ways. The device can be controlled with 2x16 LCD screen and 6 buttons as well as wirelessly controlled by a computer or mobile device. Raspberry Pi Zero Wireless will be used as a development board in order to enable the device to perform all desired functions. As the operating system, a Linux-based operating system that will be compiled specifically for this work will be used in order to reduce the cost by running the device faster and saving storage space at the same time, and the control software will be written in Python language. However, if necessary, different languages ​​can be used. The card will be powered by a 5V 3A adapter. The STD MTR QK1-4640 24V 9000 RPM DC motor, which will ensure the rotation of the surface to be coated, was chosen arbitrarily in line with the facilities available and provided free of charge. Any engine with sufficient specification can be used. L298 Engine, which will drive integrated circuit, the engine can take in enough speed and is the most suitable driver circuit sold in Turkey. The motor and driver circuit will be fed by a 19V 3.42A Adapter and will provide the required power for the desired performance. The speed of the motor will be measured by the LM393 integrated infrared speed sensor circuit. By using the signals received from the infrared sensor, the engine speed will be kept constant at the desired speed with a control system. Plastic junction box with dimensions of 210mm x 280mm x 138.5mm was preferred for the outer casing of the device in terms of its flexible structure and strength. The disc on which the surface to be coated will sit, the parts that will hold the surface and the disc that will be used to count the engine speed will be produced by 3D printing. The transparent inner wall and outer cover for protection will be made of materials that can be found easily and cheaply in the markets.

One of the leading situations that may hinder the progress of the work is the risk of not proper engine and disc balance. Roughness and errors may occur in 3D printer prints. This imbalance may cause an oscillating movement due to an increase in motor speed. In this case, the oscillation movement will cause the motor or other rotating structures to deteriorate after a while. In order to prevent such a problem, the maximum engine speed can be limited to a speed lower than 7200 RPM within the framework of the results obtained by carrying out necessary tests.

Another factor that needs to be reviewed is the low stabilization that can occur at low revs. The motor may or may not turn with a higher margin of error than expected below a certain speed. In such a case, it may be necessary to increase the minimum speed above a certain level.

## References

[1] Bianchi, R., Pansierra, M., Lima, J., Yagura, L., Andrade, A. Faria, R. 2006. “Spin coater based on brushless dc motor of hard disk drivers”, Progress in Organic Coatings, 57, 33-36.

[2]Sadegh-cheri,M.2016. “Design,Fabrication,andOpticalCharacterizationofaLow-Costand Open-Source Spin Coater”, J. Chem. Educ., 96, 1268-1272.

## Images
Images will be added as soon as possible.

## Manual
Manual will be added as soon as possible.

