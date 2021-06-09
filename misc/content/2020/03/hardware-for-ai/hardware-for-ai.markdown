Status: published
Date: 2021-04-11 11:56:25
Author: Benjamin Du
Slug: hardware-for-ai
Title: Hardware for AI
Category: AI
Tags: AI, deep learning, machine learning, data science, hardware, GPU, TPU, Jetson Nano, Google Coral

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

[TVM](https://github.com/apache/incubator-tvm)
for deep learning is kind of like LLVM for programming languages.


[Nvidia TensorRT](https://developer.nvidia.com/tensorrt)


## Embedded/Edge AI

Jetson Nano

Google Coral

Intel Neural Compute Stick 2

https://heartbeat.fritz.ai/edge-tpu-google-coral-usb-accelerator-cf0d79c7ec56

https://blog.usejournal.com/google-coral-edge-tpu-vs-nvidia-jetson-nano-a-quick-deep-dive-into-edgeai-performance-bc7860b8d87a

https://mp.weixin.qq.com/s/NtnTQIecFq1L1ffPnirMIA

## Tutorials

https://mp.weixin.qq.com/s/mId2Y4Do2k67pKq1WDVm8A

https://mp.weixin.qq.com/s/IraqkibhGciJ37sKoGxyvg

CPU：i9-10920X
显卡GPU：七彩虹RTX3090 Advance
内存：芝奇幻光戟16G x 4共64G
主板：华硕X299-DELUXE PRIME
固态硬盘：1TB西数NVME SSD + 1TB三星870QVO SATA SSD
机械硬盘：希捷EXOS 12TB氦气盘
电源：海盗船AX1200i 1200W模组电源
散热器：海盗船H100X240水冷 + 若干120机箱风扇
机箱：海盗船AIR540 E-ATX机箱

- 最佳性价比GPU：RTX 2070
- 避免的坑：所有Tesla、Quadro、创始人版（Founders Edition）的显卡，还有Titan RTX、Titan V、Titan XP
- 高性价比：RTX 2070（高端），RTX 2060或GTX 1060 (6GB)（中低端）
- 穷人之选：GTX 1060 (6GB)
- 破产之选：GTX 1050 Ti（4GB），或者CPU（原型）+ AWS / TPU（训练），或者Colab
- Kaggle竞赛：RTX 2070
- 计算机视觉或机器翻译研究人员：采用鼓风设计的GTX 2080 Ti，如果训练非常大的网络，请选择RTX Titans
- NLP研究人员：RTX 2080 Ti
- 已经开始研究深度学习：RTX 2070起步，以后按需添置更多RTX 2070
- 尝试入门深度学习：GTX 1050 Ti（2GB或4GB显存）


https://www.digitalstorm.com/configurator.asp?id=3137888

Need UPS in case of power interruption 

https://list.jd.com/Search?keyword=%E5%8F%B0%E5%BC%8F%E6%9C%BA%E6%96%AD%E7%94%B5%E4%BF%9D%E6%8A%A4%E7%94%B5%E6%BA%90&enc=utf-8&spm=2.1.11