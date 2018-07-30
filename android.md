# 全屏：
```java
	private final int fullScreenParam = View.SYSTEM_UI_FLAG_LAYOUT_STABLE
	        | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
	        | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
	        | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION // hide nav bar
	        | View.SYSTEM_UI_FLAG_FULLSCREEN // hide status bar
	        | View.SYSTEM_UI_FLAG_IMMERSIVE;

	mView.setSystemUiVisibility(fullScreenParam);
```
#String encryption
```java
	public static String getEncryption(String para) {
		int key = 0x10;
		char[] charArray = para.toCharArray();
		for (int i = 0; i < charArray.length; i++) {
			charArray[i] = (char) (charArray[i] ^ key);
		}
		return String.valueOf(charArray);
	}
```


	ijkMediaPlayer.setOption(IjkMediaPlayer.OPT_CATEGORY_PLAYER, "soundtouch", 1);
	
#在截屏的时候
		xml 中 scrollview 必须加上 android:orientation="vertical" 否则超出屏幕部分会是黑屏。

# jni
```java
	#include <jni.h>
	#include <string.h>
	#include <android/log.h>
	#include <unistd.h>  
	#include <sys/stat.h>  
	#include <sys/time.h>  
	#include <stdlib.h>  
	#include <fcntl.h>

	#define LOGI(...) __android_log_print(ANDROID_LOG_INFO  , "liqiong_file", __VA_ARGS__)
	#ifdef __cplusplus
	extern "C" {
	#endif

	JNIEXPORT jstring JNICALL Java_com_chazuo_college_enterprise_jni_MediaFileEncrypt_encrypt(
			JNIEnv*, jclass, jstring,jstring);


	#ifdef __cplusplus
	}
	#endif

	JNIEXPORT jstring JNICALL Java_com_chazuo_college_enterprise_jni_MediaFileEncrypt_encrypt(
			JNIEnv* env, jclass clazz,jstring r_path,jstring w_path) {
		const char* r_path_jni;
	   	r_path_jni = env->GetStringUTFChars(r_path, false);
	   	const char* w_path_jni;
	   	w_path_jni = env->GetStringUTFChars(w_path, false);
		FILE * file_r=fopen(r_path_jni, "rb");
		FILE * file_w=fopen(w_path_jni, "wb");

		char fBuffer[2048];

		while(!feof(file_r)){
			fread(fBuffer, 1, 2048, file_r);
			for (int i = 0; i < sizeof(fBuffer); ++i)
			{
				fBuffer[i]=fBuffer[i]^0x71;	
			}
			fwrite(fBuffer,1,2048,file_w);
		}
		fclose(file_r);
		fclose(file_w);
		LOGI("success!");

		// char * buffer[50];
		// FILE * fp = fopen("/storage/emulated/0/fuck.txt", "r");
		// fread(buffer,1,sizeof(buffer),fp);
		// fclose(fp);
		// LOGI("======%s",buffer);



		// const char* r_path_jni;
	 //   	r_path_jni = env->GetStringUTFChars(r_path, false);

	 //   	const char* w_path_jni;
	 //   	w_path_jni = env->GetStringUTFChars(w_path, false);
	   	
		// FILE * file_r=fopen(r_path_jni, "rb");
		// FILE * file_w=fopen(w_path_jni, "wb");

		// if(file_r == NULL || file_r == NULL) {
		//     printf("file open field");
		//     return (env)->NewStringUTF("file open field");
		// }

		// int ch;
	 //    int i = 0;
	 //    int pwd = 0x71;

	 //    while ((ch = fgetc(file_r)) != EOF) {
	 //    	i++;
		//     fputc(ch^pwd, file_w);	
	 //    }
	 //    fclose(file_r);
	 //    fclose(file_w);
		return (env)->NewStringUTF("xxx");
	}
```

# rom
	fastboot flash recovery recovery.img     刷入recovery.img
	
# webview 5.0以上不支持http 和https 混编
	        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            webSettings.setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW);
        }


# 全屏幕 点击显示 视频
	private void hideStatusBarNavigation(){
        rootView.setSystemUiVisibility(View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_FULLSCREEN
                | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY);
    }
# 全屏幕 正常观看
    private void showStatusBarNavigation(){
        rootView.setSystemUiVisibility(View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN);
    }

# adb录制视频
	adb shell screenrecord /sdcard/demo.mp4


# 超级大图，模糊处理
ImagePipelineConfig config = ImagePipelineConfig.newBuilder(getApplicationContext())
            .setDownsampleEnabled(true)
            .build();

Fresco.initialize(getApplicationContext(), config);

ijkPlayer 去掉log
	 	#define VLOG(level, TAG, ...)    
		#define ALOG(level, TAG, ...)    
		把实现print去掉即可