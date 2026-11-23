# Neuro-X

Multimodal AI platform for pre-symptomatic Alzheimer's disease prediction, combining 3D structural neuroimaging, clinical/tabular fusion, and a web-based diagnostic viewer.

## Repository Structure

```text
Neuro-X/
├── notebooks/
│   └── setup_colab.ipynb       # Standard Colab environment, Drive mount, and Git sync
├── src/
│   ├── neuroimaging/           # MRI preprocessing, PyTorch/MONAI 3D models, GCNN connectome
│   └── fusion/                 # Multimodal feature fusion, Scikit-Learn, XGBoost, ONNX export
├── backend/                    # FastAPI server & PostgreSQL integration
├── frontend/                   # React.js UI & Cornerstone.js DICOM viewer
├── .gitignore                  # Blocks datasets, medical scans, model weights, and secrets
└── README.md
```

## Team & Module Ownership

| Member | Focus Area | Primary Stack | Target Directory |
| :--- | :--- | :--- | :--- |
| **Nemika** | Neuroimaging AI | PyTorch, MONAI, 3D MRI, GCNN | `src/neuroimaging/` |
| **Najah** | Fusion & Optimization | Scikit-Learn, XGBoost, ONNX | `src/fusion/` |
| **Kavinu** | Full-Stack Web | FastAPI, React.js, PostgreSQL, Cornerstone.js | `backend/`, `frontend/` |

---

## 1. One-Time Dataset Setup (Google Drive)

Datasets and model weights are stored in Google Drive—**never commit raw scans, `.zip` archives, or checkpoints to GitHub**.

1. Open Google Drive and navigate to **Shared with me**.
2. Locate the shared `Neuro-X_Data` folder:
   * `Dataset/` — **Viewer** access (read-only raw archives).
   * `Checkpoints/` — **Editor** access (shared model weights and experiment logs).
3. Right-click `Neuro-X_Data` and select **Organize > Add shortcut > My Drive** (place it directly in the root of **My Drive**).

Once the shortcut is in place, every team member accesses the exact same mounted path inside Colab:
* **Dataset path:** `/content/drive/MyDrive/Neuro-X_Data/Dataset`
* **Checkpoints path:** `/content/drive/MyDrive/Neuro-X_Data/Checkpoints`

### Available Archives

| File | Size | Purpose |
| :--- | :--- | :--- |
| `sampleee_dataset.zip` | ~1.4 MB | Fast local testing and pipeline debugging (`USE_FULL_DATASET = False`) |
| `samplee.zip` | ~24.43 GB | Full training dataset (`USE_FULL_DATASET = True`) |

> **Important:** Always extract archives into Colab's temporary local SSD (`/content/local_dataset`). Never unzip datasets directly inside `/content/drive/MyDrive/`.

---

## 2. Running in Google Colab

### Configure Your GitHub Token (One-Time)
1. On GitHub, go to **Settings > Developer settings > Personal access tokens > Fine-grained tokens** and generate a token scoped strictly to `NemikaA/Neuro-X` with **Contents: Read and write** permission.
2. In Google Colab, open the **Secrets (key icon)** panel on the left sidebar.
3. Add a secret named `GITHUB_TOKEN`, paste your token, and enable **Notebook access**.

### Start a Session
1. Open Google Colab and go to **File > Open notebook > GitHub**.
2. Select `NemikaA/Neuro-X`, pick your working branch, and open `notebooks/setup_colab.ipynb`.
3. Update `GITHUB_USER` and `BRANCH_NAME` in Cell 2 to match your GitHub username and branch.
4. Keep the runtime on **CPU** while writing or debugging preprocessing code to preserve free GPU quota; switch to **Runtime > Change runtime type > T4 GPU** when running PyTorch/MONAI training.
5. Run Cells 1–4 in order to mount Drive, sync the repo to `/content/Neuro-X`, extract the dataset to `/content/local_dataset`, and verify PyTorch device availability.

---

## 3. Git & Collaboration Rules

* **Work on feature branches:** Create a dedicated branch per task (e.g., `feature/mri-preprocessing`, `feature/xgboost-fusion`, `feature/dicom-viewer`) and open a Pull Request into `main`.
* **Keep reusable logic in `src/`:** Place data loaders, preprocessing transforms, and model classes in `.py` modules inside `src/` and import them from notebooks to avoid `.ipynb` merge conflicts.
* **Clear outputs before committing notebooks:** In Colab, run **Edit > Clear all outputs** before saving `.ipynb` changes to GitHub.
* **Never commit secrets or data:** Verify `git status` before pushing. `.gitignore` already blocks `.zip`, `.nii`, `.nii.gz`, `.dcm`, `.pt`, `.pth`, `.onnx`, `.csv`, and `.env` files.