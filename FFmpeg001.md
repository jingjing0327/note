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

FFmpeg库简介：
ffmpeg一个包含8个库
	avcodec：编解码（最重要的库）
	avformat：封装格式处理
	avfilter：滤镜特效处理
	avdevice：各种设备的输入输出
	avutil：工具库（大部分库都需要这个库的支持）
	postproc：后加工
	swresample：音频采样数据格式转换
	swscale：视频像素数据格式转换

ffmpeg解码函数的作用
	av_register_all()：注册所有组件
	acformat_open_input():打开输入视频文件
	avformat_find_stream_info():获取视频文件信息
	avcodec_find_decoder():查找解码器
	avcodec_open2():打开解码器
	av_read_frame():从输入文件读取一帧压缩数据
	avcodec_devode_video2():解码一帧压缩数据
	avcodec_close():关闭解码器
	avformat_close_input():关闭输入视频文件