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