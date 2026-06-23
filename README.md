\# Redrob AI Ranker



AI-powered candidate ranking system built for the India Runs Data \& AI Challenge.



\## Approach



1\. Extract skills from the Job Description.

2\. Generate candidate profiles.

3\. Create semantic embeddings using Sentence Transformers.

4\. Build FAISS index for fast retrieval.

5\. Retrieve Top 500 semantic matches.

6\. Apply hybrid ranking using:

&#x20;  - Semantic Similarity Score

&#x20;  - AI Skill Score

&#x20;  - Experience Score

7\. Generate Top 100 shortlisted candidates.



\## Tech Stack



\- Python

\- Sentence Transformers

\- FAISS

\- NumPy

\- Pandas



\## Repository Structure



\- src/ : Source code

\- data/ : Input files

\- requirements.txt : Dependencies

\- submission\_metadata.yaml : Submission metadata



\## Output



The final submission is generated as:



output/submission.csv

