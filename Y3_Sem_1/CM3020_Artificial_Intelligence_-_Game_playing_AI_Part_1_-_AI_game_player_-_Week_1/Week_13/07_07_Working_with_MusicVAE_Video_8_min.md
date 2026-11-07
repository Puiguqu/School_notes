# 07_Working_with_MusicVAE_Video_8_min

# Working with MusicVAE
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/tdvx2/working-with-musicvae

This technical summary details the workflow for utilizing MusicVAE, a generative musical library, demonstrating the steps from environment setup to latent space sampling and output analysis.

The process begins with preparation, requiring the installation of necessary node modules via `npm install`, which serves as the dependency manager, analogous to `pip install` in Python. Following this, a local web server must be initialized, as the MusicVAE JavaScript library depends on serving its models from a web source. This local server, often running on port 8080, allows the model files—which can include complex multi-track models (e.g., 8/16 part models with bass, drums, and melody)—to be downloaded.

The core workflow involves loading a specific MusicVAE model, such as a one-bar or 16-bar model, into the script environment. The model is instantiated and requires a URL pointing to the newly created local web server for access.

