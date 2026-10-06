# SPRINT1 — Fidelity-Aware Low-Light Image Enhancement

## 1. Mission

Our mission is to help photographers enhance low-light images while providing information about which parts of the enhanced result may be less reliable.

## 2. Target User

Our primary user is a photographer who frequently works with low-light images and uses computational or AI-based enhancement tools in post-processing.

The photographer wants to recover visibility and useful detail from underexposed images while also understanding which regions of the enhanced result may deserve additional inspection.

## 3. User Stories

### User Story 1 — Load a Low-Light Image
As a photographer, I want to provide a low-light image to the system so that I can process it through the enhancement pipeline.

**Acceptance Criteria:**
- The system loads a valid image successfully.
- The original image is displayed correctly.

### User Story 2 — Enhance the Image
As a photographer, I want the system to enhance my low-light image so that dark regions become more visible.

**Acceptance Criteria:**
- The system produces an enhanced output.
- The enhanced image can be displayed and saved.
- The same enhancement method can be applied reproducibly.

### User Story 3 — Generate a Fidelity Indicator
As a photographer, I want additional information about the stability of the enhanced result so that I can identify regions that may deserve closer inspection.

**Acceptance Criteria:**
- The system applies a controlled perturbation to the input.
- It compares outputs before and after perturbation.
- It produces an output-sensitivity map.

### User Story 4 — Compare Enhancement and Indicator
As a photographer, I want to view the input, enhanced image, and indicator together so that I can make a more informed editing decision.

**Acceptance Criteria:**
- The system displays the low-light input, enhanced output, and indicator.
- The visualizations are spatially aligned and interpretable.

### User Story 5 — Validate the Indicator
As a researcher/developer, I want to compare the proposed indicator with paired reference images so that I can test whether it is actually related to enhancement error.

**Acceptance Criteria:**
- A reference-error map is computed from paired data.
- Correlation between sensitivity and reference error is measured.
- The proposed indicator is compared with a simple brightness/darkness baseline.

## 4. Feasibility

We verified the basic feasibility of the project using the LOL paired low-light dataset. We successfully downloaded the dataset and implemented a Python pipeline that loads corresponding low-light and normal-light reference images. A tested pair of 600 × 400 images was successfully loaded, displayed, and processed.

We implemented gamma correction as an initial enhancement baseline and computed a pixel-wise reference-error map. We then introduced a small controlled perturbation to the low-light input and generated an output-sensitivity map from the difference between enhanced outputs.

On our first test image, the sensitivity–error correlation was **-0.564**, the sensitivity–darkness correlation was **+0.569**, and the error–darkness correlation was **-0.969**. These preliminary results suggest that the current sensitivity indicator is strongly affected by brightness and should not yet be interpreted as a reliability measure.

## 5. Tooling

- **Python:** image processing, experiments, and quantitative evaluation.
- **NumPy:** pixel-level computation, perturbations, error maps, and correlation analysis.
- **Pillow:** image loading and manipulation.
- **Matplotlib:** visualization of inputs, outputs, error maps, and sensitivity maps.
- **LOL Dataset:** paired low-light and normal-light images for development and reference-based evaluation.
- **Gamma Correction:** simple initial enhancement baseline; a stronger existing LLIE method will be evaluated during the sprint.
- **VS Code:** local development environment.
- **GitHub:** version control, issues, project board, and documentation.

The current prototype runs locally on a MacBook using open-source libraries and has no API cost or rate limit.

## 6. Demo Sentence

At the end of two weeks, we will demonstrate an end-to-end prototype that takes a low-light image as input, enhances the image using a low-light enhancement method, generates an output-sensitivity indicator, and evaluates whether that indicator is related to enhancement error using paired reference images.

## 7. Riskiest Assumption + Test + Pivot

Our project depends on five main assumptions:

1. An existing LLIE method can be integrated into our pipeline.
2. Paired low-light/reference data are available for evaluation.
3. Small controlled input perturbations produce measurable output changes.
4. Output sensitivity contains useful information about enhancement error.
5. A meaningful fidelity indicator could help photographers inspect AI-enhanced results.

**Riskiest Assumption:** Assumption 4. If output sensitivity has no useful relationship with enhancement error, it should not be presented as a reliability indicator.

**Cheapest Test:** We apply a controlled perturbation to a low-light image, process the original and perturbed inputs using the same enhancement method, generate an output-sensitivity map, and compare it with reference-based reconstruction error.

Our first gamma-baseline test produced a sensitivity–error correlation of **-0.564**. The result does not support interpreting sensitivity directly as reliability and suggests that brightness is an important confounding factor.

**Pivot:** We change direction if output sensitivity does not show a consistent and useful relationship with reference error across multiple images and a stronger LLIE baseline. We will then investigate an alternative fidelity indicator while retaining the enhancement and reference-based evaluation pipeline.

## 8. Evaluation and Baselines

We evaluate two aspects of the project.

**Enhancement Quality:** Enhanced images will be compared with paired normal-light references using **PSNR** and **SSIM**. Gamma correction serves as our initial simple enhancement baseline.

**Fidelity Indicator:** We measure the correlation between the output-sensitivity map and reference-error map across images. Because brightness may confound sensitivity, a simple **darkness map** is used as an additional baseline.

The proposed indicator will only be considered useful if it shows a consistent relationship with reference error and provides useful information beyond the simple brightness-based baseline.

## 9. Related Work

1. **Chen et al., “Learning to See in the Dark,” CVPR 2018.** Uses paired short-exposure RAW and long-exposure images for low-light reconstruction, but does not explicitly estimate spatial output reliability.

2. **Wei et al., “Deep Retinex Decomposition for Low-Light Enhancement,” BMVC 2018.** Learns Retinex-based reflectance and illumination decomposition, but the decomposition remains highly ill-posed.

3. **Guo et al., “Zero-Reference Deep Curve Estimation for Low-Light Image Enhancement,” CVPR 2020.** Removes the need for reference images using zero-reference curve estimation, but does not directly measure reconstruction fidelity.

4. **Jiang et al., “EnlightenGAN: Deep Light Enhancement Without Paired Supervision,” IEEE TIP 2021.** Enables enhancement without paired supervision, but perceptual realism does not directly indicate scene fidelity.

5. **Liu et al., “Retinex-Inspired Unrolling with Cooperative Prior Architecture Search,” CVPR 2021.** Develops an efficient Retinex-inspired reference-free architecture, but does not explicitly provide spatial reliability information.

6. **Xu et al., “SNR-Aware Low-Light Image Enhancement,” CVPR 2022.** Uses spatial SNR information to guide enhancement, but SNR is not equivalent to actual enhancement error.

7. **Wang et al., “Low-Light Image Enhancement with Normalizing Flow,” AAAI 2022.** Models multiple possible normally exposed outputs probabilistically, but does not directly provide a user-facing spatial reconstruction-error indicator.

8. **Cai et al., “Retinexformer: One-stage Retinex-based Transformer for Low-light Image Enhancement,” ICCV 2023.** Uses illumination-guided Transformers for strong low-light restoration, but does not explicitly communicate spatial output reliability.

9. **Yi et al., “Diff-Retinex: Rethinking Low-light Image Enhancement with a Generative Diffusion Model,” ICCV 2023.** Combines Retinex decomposition with diffusion models to infer missing information, raising the question of how to distinguish recovered information from prior-generated plausible detail.

10. **Cho et al., “MR. Illuminate: Zero-Shot Low-Light Image Enhancement with Diffusion Prior,” CVPR 2026.** Uses a pretrained diffusion prior for zero-shot enhancement and generalization, but does not explicitly indicate which output regions are strongly supported by the observation versus the learned prior.

**Open Problem:** Existing LLIE methods primarily focus on enhancement quality, generalization, or perceptual realism. Our project investigates whether a simple spatial indicator can provide additional information about where an enhanced result may be less reliable when paired reference data are available for validation.

## 10. Potential Harm

1. Incorrect low-light enhancement may create visually convincing details that are not faithfully supported by the original image, potentially misleading users who rely on the enhanced result.
2. A fidelity indicator could create false confidence if users interpret it as proof that a region is physically correct rather than as an experimental estimate.
3. Our prototype will therefore present the indicator as an experimental signal, not a guarantee of reconstruction accuracy, and validate it against paired reference images before making reliability claims.
