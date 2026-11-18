# 学术原图与开放数据复绘

本报告包含 2 幅出版者原图、1 幅基于开放数据的描述性复绘，以及原创文字表格。论文图未裁切、重绘或重标注；原图文件从 Frontiers 页面所载资源直接下载。论文声明采用 CC BY 4.0，相关原图继续保留原作者署名与来源，不纳入本仓库第一方许可。

| 编号 | 类型 | 来源 / 读图用途 | 文件 |
|---|---|---|---|
| O01 | 出版者原图 | Liu et al. (2026), Figure 1：触觉输入编码、类器官刺激与分类流程 | [原图](figures/original/braille-figure-1.webp) |
| O02 | 出版者原图 | Liu et al. (2026), Figure 9：类器官输出热图、混淆矩阵、噪声准确率 | [原图](figures/original/braille-figure-9.webp) |
| D01 | 开放数据复绘 | 三类器官 24 通道数据按字母聚合的均值热图；不重跑分类器 | [复绘图](figures/derived/braille_mean_spike_counts_by_letter.png)；[脚本](figures/derived/replot_braille_organoid.py) |

## O01 · Liu et al. (2026), Figure 1 {#o01}

原图说明：展示 Evetac 触觉传感器输入被编码成电刺激，送入低密度 MEA 上的人类前脑类器官，再以神经活动输出进行 26 个 Braille 字母分类的实验流程。

出处：Tianyi Liu, Hemma Philamore, Benjamin Ward-Cherrier. “Encoding tactile stimuli for Braille recognition with organoids.” *Frontiers in Artificial Intelligence* 9 (2026), 1800219. [DOI](https://doi.org/10.3389/frai.2026.1800219)；[出版者全文及 Figure 1](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1800219/full)。

许可：论文版权声明为 CC BY 4.0。按原作者及原出版物署名转载；未改动。来源文件为出版者托管的 `frai-09-1800219-g0001.webp`。SHA256：`f1f24ce48298eacda5fc08007e81c9285117216fb6fbc3d9bf76081982023bd4`。尺寸：1417 × 567。

## O02 · Liu et al. (2026), Figure 9

原图说明：比较单类器官与三类器官输出；包含通道响应热图、26 类混淆矩阵及不同噪声条件下的分类准确率。

出处与许可同 O01。来源文件为出版者托管的 `frai-09-1800219-g0009.webp`。SHA256：`a7bf1e79888d46d71dc3f27eb2b61dec039078ac4bbaadd0b2122d29292e6c65`。尺寸：1772 × 1620。原图未改动。

## D01 · data.bris 作者数据复绘 {#d01}

复绘定义：读取数据集 `derived/three_organoid_24_channel_spike_counts.csv`，按 `braille_letter` 分组，对通道 40–63 的 24 个 `spike_count` 列分别求算术平均，按 A–Z 绘制 26 × 24 热图。数据共 1,287 行，每类 46–51 个样本。此图只描述公开输出数据的通道均值，不复现论文混淆矩阵、分类器或准确率。

来源：Ward-Cherrier, Liu & Philamore (2026), *Encoding Tactile Stimuli for Braille Recognition with Organoids*, University of Bristol data.bris, DOI [10.5523/bris.19qmlywobvl3u22pzo67z3bc6l](https://doi.org/10.5523/bris.19qmlywobvl3u22pzo67z3bc6l)。[数据集入口](https://data.bristol.ac.uk/data/dataset/19qmlywobvl3u22pzo67z3bc6l)；[下载 ZIP](https://data.bris.ac.uk/datasets/19qmlywobvl3u22pzo67z3bc6l/19qmlywobvl3u22pzo67z3bc6l.zip)。

许可：数据集页面标注为 [Non-Commercial Government Licence v2.0](https://www.nationalarchives.gov.uk/doc/non-commercial-government-licence/version/2/)。允许非商业用途复制、发布和改编，需署名并保留非商业限制。本复绘图及其数据衍生内容仅限非商业用途；此许可只适用于该数据衍生内容，不改变本仓库其他材料的许可状态。署名语句：Contains information licensed under the Non-Commercial Government Licence v2.0.

重现：在已安装 `pandas`、`numpy`、`matplotlib` 的 Python 环境中运行：

```bash
python figures/derived/replot_braille_organoid.py
```

脚本从 data.bris 下载 ZIP 到内存，只读取上述 CSV，不把原始数据包写入或转存仓库。图像输出在脚本同目录。绘图 SHA256：`e81e996414025a675441890c295373c8822f158ba5521a093b0a32591dbdfc2c`。
