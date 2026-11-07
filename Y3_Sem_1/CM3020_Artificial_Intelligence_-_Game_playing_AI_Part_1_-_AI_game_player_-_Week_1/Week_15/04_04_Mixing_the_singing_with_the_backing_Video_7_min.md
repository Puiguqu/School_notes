# 04_Mixing_the_singing_with_the_backing_Video_7_min

# Mixing the singing with the backing
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/97uw4/mixing-the-singing-with-the-backing

The primary focus of this video segment is demonstrating the final step of music production: mixing a backing track with vocal recordings using three distinct methodologies. These methods include leveraging graphical audio applications (Reaper and Audacity) and implementing a code-based workflow using Python and the Librosa library.

Reaper, a multi-track commercial application created by Justin Frankel (also the creator of Winamp), offers a powerful environment for this mixing task. The process in Reaper involves loading the tracks (e.g., `skippy.wav`) onto a blank slate and carefully adjusting levels to prevent distortion, ensuring the audio does not clip into the red zone. Since the initial singing was too fast, the workflow required substituting the original track with a pre-rendered, slower version (`skippy slow`). The slow vocal track is then manually dragged and lined up against the backing track to achieve proper synchronization.

Audacity, presented as an open-source graphical alternative suitable for various platforms, performs the same mixing task. In Audacity, tracks are also dragged and dropped into a multi-track setup. The crucial step here utilizes the "Time Shift Tool," which allows the user to visually pull and align the vocal track accurately with the accompanying music. Volume balance is then fine-tuned using the dedicated controls on the respective track channels.

The third, and most technical, method involves implementing the mix using code, relying heavily on Librosa for audio processing. The coding workflow requires several specific steps: loading the input files (singing and music), and normalizing them to maximize the available audio levels. The shorter track must then be padded with zeros at the beginning to match the length of the longer track—a programmatic equivalent of dragging the track in the graphical tools.

This padding prepares the tracks for addition using NumPy's `NumPy add` function, after which the combined audio is written out to disk as a final mixed file. The implementation script specifies the filenames, checks for their existence, and sets a sample rate, commonly 44100, for high quality. The script utilizes a pad function, essentially calling `np.pad` with appropriate parameters, which handles length differences by either padding or truncating the end of the longer track.

Overall, this video successfully demonstrated how simple track mixing can be achieved both through intuitive GUI tools like Reaper and Audacity, and through rigorous mathematical processing using Python and Librosa. While the finished composition is noted as being functional for pop music, the presenter acknowledges that achieving a polished, "big" sound requires advanced AI techniques that were beyond the scope of this basic mixing demonstration. Furthermore, the surrounding course material references broader AI topics, including genetic algorithms for creature evolution, DQN agents for game playing, and generative models like MusicVAE and DiffSinger for advanced music composition.

