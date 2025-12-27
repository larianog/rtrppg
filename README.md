# Playground for "3DCNN-based Real-Time rPPG network (RTrPPG)"

## Installation
To install an anaconda virtual enviroment with the dependencies, you can run in your anaconda prompt:
```sh
conda env create -f \...\rtrppg\rtrppg_env.yaml
```

## Usage

### Video processing
This repository has the example used in the demo of RTrPPG paper, in the demo_subject/p1v1s1 folder. However, if you want to run the model in your own example, you can add a video file in a new folder called video, and then use the video_processing.py function to create the necessary data format to run the demo.

### RTrPPG demo
This demo uses the RTrPPG network trained on the VIPL-HR database [1] to generate an RPPG signal from a video of dimensions: Batch=1, Channels=3 (YUV), Time=128, Width = 8, Height = 8. The demo runs on CPU only so that it works on all hardware. However, changing the code to work on GPU is really easy (note to install the respective packages to work on GPU).

Inside the repository folder run the following command line:
```sh
python demo.py --run rtrppg_demo
```

This demo generates the resulting RPPG signal and saves it in the repository folder as "Output.png."

![](media/Output.png)

In this repository, it is also available a python notebook that can run the demo cell by cell, facilitating the debugging and viewing of the processing data.

## Acknowledgments

- The example video used belong to the VIPL-HR database proposed by Niu, Xuesong, et al [1]. 
- The baseline network was based on the following repository: https://github.com/ZitongYu/PhysNet

## References
[1] Niu, Xuesong, Hu Han, Shiguang Shan, and Xilin Chen. "VIPL-HR: A multi-modal database for pulse estimation from less-constrained face video." In Asian conference on computer vision, pp. 562-576. Springer, Cham, 2018.

[2] D. Botina-Monsalve, Y. Benezeth and J. Miteran, "RTrPPG: An Ultra Light 3DCNN for Real-Time Remote Photoplethysmography," 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW), New Orleans, LA, USA, 2022, pp. 2145-2153, doi: 10.1109/CVPRW56347.2022.00233.
