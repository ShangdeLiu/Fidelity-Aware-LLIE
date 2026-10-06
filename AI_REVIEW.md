# AI Review Log

## Models Used

- **AI Reviewer 1:** ChatGPT
- **AI Reviewer 2:** Claude

Both models independently reviewed the same `SPRINT1.md` and answered:

1. What is our riskiest unstated assumption?
2. Why might this project fail by week 6?
3. What is missing from our evaluation?

The critiques were then exchanged between the two models for cross-review.

## Where the Reviews Agree

Both reviewers identified the same central risk: the current output-sensitivity indicator may measure image brightness or the behavior of the enhancement operator rather than actual enhancement fidelity.

Both reviewers also agreed that:

- One image and one perturbation setting are not enough to validate the indicator.
- Gamma correction alone is too weak to support a general claim about LLIE methods.
- The sensitivity indicator should be compared against a simple brightness/darkness baseline.
- Evaluation should be extended across multiple images.
- The project should pivot early if sensitivity does not provide useful information beyond simple baselines.
- Output sensitivity should not be presented as a validated reliability measure without additional evidence.

## Where the Reviews Disagree

Claude placed stronger emphasis on whether the paired normal-light reference and the resulting reference-error map are themselves valid targets for fidelity evaluation. It also recommended a broader evaluation including additional metrics, statistical analysis, stronger LLIE models, and user-facing validation.

ChatGPT agreed that reference-based error should not automatically be interpreted as absolute physical reconstruction error, but argued that the full evaluation proposed by Claude would be too broad for the current solo Sprint. ChatGPT recommended first answering the narrower question of whether sensitivity provides useful information beyond brightness before expanding the evaluation.

The reviews also differed in interpreting the initial error–darkness correlation of **-0.969**. Claude treated this as strong evidence that the reference-error map may be dominated by brightness. ChatGPT argued that this conclusion is too strong because the result comes from only one image and a gamma-correction baseline. We therefore treat the result as evidence of a possible brightness confound that requires further testing, not as a general conclusion.

## Project Decision

After considering both reviews, the project will keep the current scope but strengthen the validation protocol.

The next evaluation will test multiple LOL image pairs and explicitly compare output sensitivity with a darkness baseline. We will also investigate whether sensitivity provides information about reference-based error after accounting for brightness.

If feasible within the Sprint, we will test the same idea with one stronger existing LLIE method in addition to gamma correction.

We will continue to use the term **reference-based error** rather than treating the paired reference as absolute physical ground truth.

## Change Made Because of the AI Review

The original evaluation focused primarily on the correlation between output sensitivity and reference error.

After the two-model review, we changed the evaluation question to:

> **Does output sensitivity provide useful information about reference-based enhancement error beyond what can already be explained by image brightness?**

The updated evaluation will therefore include:

- Multiple LOL evaluation images
- Sensitivity–error comparison
- Darkness–error baseline comparison
- Brightness-controlled analysis where feasible
- More than one perturbation strength
- One stronger LLIE baseline if it can be integrated reproducibly

## Pivot Rule

If output sensitivity does not provide consistent information beyond the brightness/darkness baseline, we will stop treating perturbation sensitivity as the primary fidelity indicator and investigate an alternative indicator while retaining the low-light enhancement and reference-based evaluation pipeline.

## Review Links

- ChatGPT review: [add conversation link]
- Claude review: [add conversation link]
