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