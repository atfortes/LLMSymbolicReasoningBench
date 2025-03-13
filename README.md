# Simple Synthetic Benchmarks for Language Models

This repository is dedicated to generating datasets for symbolic and logic reasoning tasks in LLMs. Our goal is to provide an implementation for the generation of datasets that are not public or do not have an official implementation, and to make it easy for people to create and reproduce them.

We encourage contributions and feedback to make this repository a valuable resource for the community. If you have any questions or suggestions, please feel free to open an issue or submit a pull request.

## Make Your Pull Requests (PRs)
If you want to contribute, we encourage you to make a PR to this repository according to the following guidelines.

### Directory Structure
Each PR should include the code and markdown description in a subdirectory.
An example subdirectory tree:

```
└── LLMSymbolicReasoningBench
    └── <Your PR directory>: Dataset name
        ├── example.json (Optional)
        ├── README.md
        ├── requirements.txt
        └── <Your code>
```

Please exclude large data files in the PR as they take up too much space. Instead, describe the method to acquire the data in your `README.md` and optionally provide a small generation snippet (`example.json`). See the `coin-flip` and `last-letter-concatenation` subdirectories for an example.

### Task Description (README.md)
Please include the following sections in your README to help its better use:

+ **Dataset Name**: Serves as the markdown title.
+ **Authors**: Your name(s), contact and/or url to your homepage (if available).
+ **Task Description**: A short paragraph to briefly introduce what the dataset and corresponding task is about.
+ **Running Commands**: Instructions for generating the dataset.
+ **Reference**: Proper citation information for the dataset (if applicable).

### Environment Requirements (requirements.txt)
Please include the necessary packages in the file for generating the dataset.

## Other Relevant Datasets

- [Reversal Curse](https://huggingface.co/datasets/lberglund/reversal_curse)

## Citation

If you find our work useful, please cite the respective datasets you used (if applicable) and this repository:

```bibtex
@misc{fortes2023LLMSymbolicReasoningBench,
    author = {Fortes, Armando},
    title = {LLMSymbolicReasoningBench},
    year = {2023},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://github.com/atfortes/LLMSymbolicReasoningBench}}
}
```
