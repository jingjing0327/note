YUV
SDL
BMP图片
H.264
AVC

ffmpeg 流程：
	start
	av_register_all()
	acformat_open_input()
	ac_find_stream_info()
	avcodec_find_decoder()
	avcodec_open()
	av_read_frame()


SDL
	SDL_Init()
	SDL_SetVideoMode()
	SDL_Surface
	SDL_CreateYUVOverlay()
	SDL_Overlay
	SDL_DisplayYUVOverlay()--解码--YUV--SDL_Overlay


解协议，解封装，解码视音频，视音频同步。

解封装，解码视音频，视音频同步。

