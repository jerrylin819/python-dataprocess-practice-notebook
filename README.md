# Python 數據處理練習筆記

這是一個Python學習筆記專案，記錄了在數據處理、分析和視覺化方面的基本操作和最佳實踐。忘記時可以來此查找使用。

## 📚 專案內容

本專案包含以下主要學習模組：

### 1. **pandas 以及 numpy 練習** (`pandas以及numpy練習.py`)
Pandas 和 NumPy 的核心操作教學：
- **numpy陣列基礎**：列表轉換、數據類型統一
- **Pandas Series**：一維數據結構、索引操作
- **Pandas DataFrame**：二維數據結構、數據框操作
- **數據選擇**：使用 `.loc` 和 `.iloc` 進行標籤和位置選擇
- **條件篩選**：使用布林索引和 `.isin()` 方法
- **數據運算**：使用 `.apply()` 和 `.map()` 進行元素和列級運算
- **數據分組**：使用 `.groupby()` 進行分組聚合運算

### 2. **資料處理練習** (`資料處理練習.py`)
實際的數據處理和清理技巧：
- **缺失值處理**：使用 `dropna()`、`fillna()` 處理空值
  - 刪除含缺失值的行或列
  - 使用平均值、眾數、中位數、最小值填補缺失值
- **類別資料處理**：轉換文字型資料為數值
  - 使用 `map()` 進行類別映射
  - 使用 `get_dummies()` 進行獨熱編碼 (One-Hot Encoding)
  - 使用 `pd.concat()` 合併資料框
- **資料正規化**：將資料縮放到 0 到 1 之間
  - 最小-最大正規化公式：`(x - x_min) / (x_max - x_min)`
- **資料標準化**：將資料轉換為平均值 0、標準差 1
  - 標準化公式：`(x - μ) / σ`

### 3. **載入 iris 資料練習** (`載入iris資料練習.py`)
使用 scikit-learn 的 iris 數據集進行數據加載和探索：
- 從 sklearn 載入 iris 數據集
- 提取特徵和目標變數
- 使用 DataFrame 合併資料
- 將數值標籤對應至名稱標籤

### 4. **網路上抓取資料練習** (`網路上抓取資料練習.py`)
網路爬蟲和數據獲取基礎：
- 使用 `requests` 套件從 API 取得數據
- 解析 JSON 格式的回應
- 將 API 數據轉換成 pandas DataFrame

### 5. **視覺化練習** (`視覺化練習.py`)
多種數據視覺化工具的使用：

#### **Matplotlib**：基礎繪圖
- 線圖、柱狀圖、散點圖
- 線條樣式設定（顏色、線型、標記符號）
- 坐標軸範圍、標籤和標題設定
- 圖表樣式切換（ggplot、classic）

#### **Pandas Plot**：快速繪圖
- 散點圖繪製
- 顏色和透明度設定
- 多圖層疊加
- 圖例和標籤

#### **Seaborn**：統計視覺化
- 線性迴歸圖 (`lmplot`)
- 色調分類展示 (`hue` 參數)
- 回歸線顯示控制

#### **Plotly**：互動式圖表
- 2D 散點圖（帶有圖例和模式設定）
- 3D 散點圖（使用多變量常態分布）
- 顏色階度設定
- 互動式操作和放大縮小

## 🛠️ 環境要求

- Python 3.7+
- Anaconda 或 Miniconda

## 📦 主要依賴

- `numpy`：數值計算
- `pandas`：數據處理和分析
- `matplotlib`：數據視覺化
- `seaborn`：統計視覺化
- `plotly`：互動式視覺化
- `scikit-learn`：機器學習和數據集
- `requests`：HTTP 請求和網路爬蟲

## 🚀 快速開始

### 1. 克隆專案
```bash
git clone https://github.com/jerrylin819/python-dataprocess-practice-notebook.git
cd python-dataprocess-practice-notebook
```
### 2.建立虛擬環境（使用 Conda）
### 方法一：手動建立虛擬環境
```bash
# 建立虛擬環境（名稱為 python-practice）
conda create --name python-practice python=3.9

# 啟動虛擬環境
conda activate python-practice

# 安裝必需的套件
conda install numpy pandas matplotlib seaborn plotly scikit-learn requests
```
### 方法二：使用 environment.yml 文件（如果有的話）
```bash
conda env create -f environment.yml
conda activate python-practice
```
### 3. 執行練習文件
```bash
# 執行 pandas 和 numpy 練習
python pandas以及numpy練習.py

# 執行資料處理練習
python 資料處理練習.py

# 執行載入 iris 資料練習
python 載入iris資料練習.py

# 執行網路資料抓取練習
python 網路上抓取資料練習.py

# 執行視覺化練習（會顯示互動式圖表）
python 視覺化練習.py
```
### 4. 停用虛擬環境
```bash
conda deactivate
```
## 📖 使用指南
每個Python文件都包含詳細的中文註釋，說明每個操作的用途。你可以：

**直接閱讀** - 查看相關的程式碼和註釋

**修改練習** - 根據需要修改代碼參數進行實驗

**參考查詢** - 需要特定操作時查找相應的程式碼片段

**取消註釋** - 許多代碼行被註釋，可以取消註釋後測試執行


## 📝 常用 Conda 指令
```bash
# 查看所有虛擬環境
conda env list

# 刪除虛擬環境
conda env remove --name python-practice

# 安裝特定版本的套件
conda install numpy=1.21.0

# 更新套件
conda update numpy

# 導出虛擬環境設定
conda env export > environment.yml

# 查看虛擬環境中已安裝的套件
conda list

# 搜尋可用的套件版本
conda search numpy

# 在虛擬環境中安裝套件
conda install -n python-practice pandas
```
## 📝 注意事項
1. 所有練習文件都使用 iris 數據集或隨機生成的數據
2. 某些代碼行被註釋，可以取消註釋進行測試
3. 確保已啟動虛擬環境且安裝所有依賴套件才能正確執行
4. 網路爬蟲練習（網路上抓取資料練習.py）需要網際網路連接
5. 視覺化練習會開啟圖表視窗，需要圖形界面支援

## 🤝 貢獻
如果你有改進建議或發現錯誤，歡迎提出 Issue 或 Pull Request。

## 📄 授權
本專案為個人學習筆記，可自由使用和參考。

**最後更新**：2026年5月

如有任何問題或建議，歡迎反饋！
