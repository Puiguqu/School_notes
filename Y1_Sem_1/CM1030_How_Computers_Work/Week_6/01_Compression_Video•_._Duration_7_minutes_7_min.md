# Compression Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/3JO2k/compression)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Compression algorithms are used to reduce the size of large files such as images and videos to make them more efficient for storage and transmission over the internet. Data compression works by representing data in a more efficient way without losing important information. Most data representations are redundant, meaning they use more bits than necessary to represent something. This redundancy can be exploited to compress data. For example, words like "the" or "and" can have very short codes of just two or three bits while rarer words have longer codes.

Compression algorithms can be lossless, which preserves the original information without losing any data, or lossy, where some data is lost to achieve better compression. Lossy compression is often used for images and audio because it can produce much better results than lossless compression, even with minimal data loss. However, lossy compression means that compressing and decompressing files multiple times can degrade the quality of the image or audio.

Run-length encoding (RLE) is a simple technique used to compress pixel values by storing only the number of consecutive identical pixels instead of each individual pixel value. RLE can be very effective for images with mostly white or black backgrounds, but it's not suitable for complex images. More sophisticated compression algorithms are needed for photographs and audio.

These algorithms transform data into a new representation that is easier to find redundant information in, such as transforming image frequencies. Lossy image, audio, and video algorithms can achieve much better compression by making the image representation more redundant while losing some information. The amount of data loss is not always noticeable, especially for everyday uses like putting an image on a webpage.

However, it's essential to remember that lossy compression does lose information, which means that repeated compressing and decompressing can degrade image or audio quality. In some cases, like archiving vintage photographs, lossless compression is preferred to ensure the highest quality possible. Compression algorithms also take time, especially when loading and using compressed files.

In conclusion, data compression is an essential technique for reducing file sizes and making data transmission more efficient. Understanding how compression algorithms work and their trade-offs between quality and size is crucial in computer science applications.

