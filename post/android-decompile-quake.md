---
title: 安卓程序反编译测试——夸克浏览器（持续更新）
tags:
  - 安卓开发
  - 破解
url: 755.html
id: 755
categories:
  - 网络技术
  - 随笔
date: 2018-06-18 22:30:34
---

![](http://file.mgek.cc/images/blog/android-quake.webp) 

基于java环境对安卓版的夸克浏览器进行反编译测试 初步涉及反编译的工作，面对成山的解包源代码文件不知从何找起，这个时候搜索就给我提供了很大的方便，如果开发者足够的良心尽责，那么所有的常用的变量的名称都是用正常的英文编写的，这样在查找的时候就比较方便。 最开始的简单编译我主要从如下的xml文档中找到源代码相关的信息进行修改 
这里用到的源代码文档为dimens（尺寸规定），login_page(登陆页），strings（文本翻译对应的文档） 1.对dimens的编辑

```java
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="abc_action_bar_home_description">Navigate home</string>
<string name="abc_action_bar_home_description_format">%1$s, %2$s</string>
<string name="abc_action_bar_home_subtitle_description_format">%1$s, %2$s, %3$s</string>
<string name="abc_action_bar_up_description">Navigate up</string>
<string name="abc_action_menu_overflow_description">More options</string>
<string name="abc_action_mode_done">Done</string>
<string name="abc_activity_chooser_view_see_all">See all</string>
<string name="abc_activitychooserview_choose_application">Choose an app</string>
<string name="abc_capital_off">OFF</string>
<string name="abc_capital_on">ON</string>
<string name="abc_search_hint">Search…</string>
<string name="abc_searchview_description_clear">Clear query</string>
<string name="abc_searchview_description_query">Search query</string>
<string name="abc_searchview_description_search">Search</string>
<string name="abc_searchview_description_submit">Submit query</string>
<string name="abc_searchview_description_voice">Voice search</string>
<string name="abc_shareactionprovider_share_with">Share with</string>
<string name="abc_shareactionprovider_share_with_application">Share with %s</string>
<string name="abc_toolbar_collapse_description">Collapse</string>
<string name="status_bar_notification_info_overflow">999+</string>
<string name="about_setting_view_forum">(｢･ω･)｢</string>
<string name="about_setting_view_privacy_agreement">基于夸克修改</string>
<string name="about_setting_view_uc">皮皮温情出品</string>
<string name="about_setting_view_useragreement">皮皮</string>
<string name="about_setting_view_webcore_info">河汉清且浅 相去复几许</string>
<string name="about_setting_window_function">功能介绍</string>
<string name="about_setting_window_share">分享给好友</string>
<string name="about_setting_window_title">关于</string>
<string name="about_setting_window_upgrade">_(:з」∠)_</string>
<string name="about_version_prefix" />
<string name="account_invalid_st">请重新登录</string>
<string name="ad_block_block_mannual_switcher">广告标记</string>
<string name="ad_block_rule_empty_view_text">没有已标识的广告</string>
<string name="ad_block_rule_title_view_text">已添加的广告规则</string>
<string name="ad_block_rule_view_delete_text">删除</string>
<string name="ad_block_rule_window_title">广告过滤</string>
<string name="add_favorite">收藏到夸克</string>
<string name="allinnavi">精选站点</string>
<string name="app_name">夸克</string>
<string name="app_name_in_launcher">夸克</string>
```

对部分的xml中的注释进行修改达到修改全局内文字翻译的效果 2.login界面修改

```xml
<?xml version="1.0" encoding="utf-8" ?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="0.0dip" android:layout_height="0.0dip">
	<LinearLayout android:gravity="center_vertical" android:orientation="horizontal" android:layout_width="0.0dip" android:layout_height="0.0dip" android:layout_marginTop="0.0dip" android:layout_marginBottom="0.0dip">
		<ImageView android:id="@id/personal_login_image" android:layout_width="0.0dip" android:layout_height="0.0dip" android:layout_marginLeft="0.0dip" />
		<LinearLayout android:orientation="vertical" android:layout_width="0.0dip" android:layout_height="0.0dip" android:layout_marginLeft="0.0dip">
			<TextView android:textSize="0.0dip" android:id="@id/personal_login_title" android:layout_width="0.0dip" android:layout_height="0.0dip" android:text="@string/personal_login_page_title" />
			<TextView android:textSize="0.0dip" android:id="@id/personal_login_subtitle" android:layout_width="0.0dip" android:layout_height="0.0dip" android:layout_marginTop="0.0dip" android:text="@string/personal_login_page_subtitle" />
		</LinearLayout>
	</LinearLayout>
	<LinearLayout android:orientation="vertical" android:id="@id/personal_login_phone_container" android:layout_width="0.0dip" android:layout_height="0.0dip" android:layout_marginLeft="0.0dip" android:layout_marginRight="0.0dip">
		<com.ucweb.materialedittext.MaterialEditText android:textSize="0.0dip" android:id="@id/personal_login_phone_edit" android:layout_width="0.0dip" android:layout_height="0.0dip" />
		<TextView android:textSize="0.0dip" android:layout_gravity="right" android:id="@id/personal_login_get_idcode_btn" android:paddingTop="0.0dip" android:paddingBottom="0.0dip" android:layout_width="0.0dip" android:layout_height="0.0dip" android:text="@string/cloud_sync_get_verif_code" android:singleLine="true" />
	</LinearLayout>
	<FrameLayout android:id="@id/personal_login_idcode_container" android:visibility="gone" android:layout_width="0.0dip" android:layout_height="0.0dip" android:layout_marginLeft="0.0dip" android:layout_marginRight="0.0dip">
		<LinearLayout android:orientation="vertical" android:layout_width="0.0dip" android:layout_height="0.0dip">
			<com.ucweb.materialedittext.MaterialEditText android:textSize="0.0dip" android:id="@id/personal_login_idcode_edit" android:layout_width="0.0dip" android:layout_height="0.0dip" />
			<TextView android:textSize="0.0dip" android:layout_gravity="right" android:id="@id/personal_login_retrieve_idcode_btn" android:paddingTop="0.0dip" android:paddingBottom="0.0dip" android:layout_width="0.0dip" android:layout_height="0.0dip" android:text="@string/cloud_sync_again_verif_code" android:singleLine="true" />
		</LinearLayout>
		<TextView android:textSize="0.0dip" android:gravity="center" android:layout_gravity="right" android:id="@id/personal_login_send_tip" android:paddingLeft="0.0dip" android:paddingRight="0.0dip" android:layout_width="0.0dip" android:layout_height="0.0dip" android:layout_marginTop="0.0dip" android:text="已发送到18920787888" />
	</FrameLayout>
	<View android:layout_width="0.0dip" android:layout_height="0.0dip" android:layout_weight="1.0" />
	<LinearLayout android:layout_gravity="center_horizontal" android:orientation="horizontal" android:layout_width="0.0dip" android:layout_height="0.0dip" android:layout_marginBottom="16.0dip">
		<ImageView android:id="@id/personal_login_weibo" android:padding="0.0dip" android:layout_width="0.0dip" android:layout_height="0.0dip" android:layout_marginRight="0.0dip" />
		<ImageView android:id="@id/personal_login_weixin" android:padding="0.0dip" android:layout_width="0.0dip" android:layout_height="0.0dip" android:layout_marginRight="0.0dip" />
		<ImageView android:id="@id/personal_login_qq" android:padding="0.0dip" android:layout_width="0.0dip" android:layout_height="0.0dip" />
	</LinearLayout>
</LinearLayout>
```


这里把所有关于登陆的窗口全部设置为0尺寸达到去掉登陆界面的目的 3.dimens修改

```xml
<dimen name="dicover_page_bookmark_item_arrow_marginright">2.0dip</dimen>
<dimen name="dicover_page_bookmark_item_height">50.0dip</dimen>
<dimen name="dicover_page_bookmark_item_icon_marginleft">24.0dip</dimen>
<dimen name="dicover_page_bookmark_item_icon_size">22.0dip</dimen>
<dimen name="dicover_page_bookmark_item_inner_icon_size">16.0dip</dimen>
<dimen name="dicover_page_bookmark_item_title_marginleft">18.0dip</dimen>
<dimen name="dicover_page_bookmark_item_title_marginright">16.0dip</dimen>
<dimen name="dicover_page_bookmark_item_title_size">14.0dip</dimen>
<dimen name="dicover_page_close_btn_width">22.0dip</dimen>
<dimen name="dicover_page_close_container_width">100.0dip</dimen>
<dimen name="dicover_page_gridview_column_width">66.0dip</dimen>
<dimen name="dicover_page_lightapp_item_extend_add_margin_right">4.0dip</dimen>
<dimen name="dicover_page_lightapp_item_extend_add_width">30.0dip</dimen>
<dimen name="dicover_page_lightapp_item_extend_category_margin_bottom">3.0dip</dimen>
<dimen name="dicover_page_lightapp_item_extend_category_textsize">10.0dip</dimen>
<dimen name="dicover_page_lightapp_item_extend_height">66.0dip</dimen>
<dimen name="dicover_page_lightapp_item_extend_icon_margin_left">12.0dip</dimen>
<dimen name="dicover_page_lightapp_item_extend_icon_margin_right">16.0dip</dimen>
<dimen name="dicover_page_lightapp_item_extend_icon_width">40.0dip</dimen>
<dimen name="dicover_page_lightapp_item_extend_space">12.0dip</dimen>
<dimen name="dicover_page_lightapp_item_extend_title_width">52.0dip</dimen>
<dimen name="dicover_page_lightapp_item_icon_margin_bottom">10.0dip</dimen>
<dimen name="dicover_page_lightapp_item_icon_width">56.0dip</dimen>
<dimen name="dicover_page_lightapp_item_textsize">12.0dip</dimen>
<dimen name="dicover_page_lightapp_item_title_margin_bottom">26.0dip</dimen>
<dimen name="dicover_page_padding_left">24.0dip</dimen>
<dimen name="dicover_page_plugin_container_margin_bottom">10.0dip</dimen>
<dimen name="dicover_page_plugin_item_btn_height">30.0dip</dimen>
<dimen name="dicover_page_plugin_item_btn_width">30.0dip</dimen>
<dimen name="dicover_page_plugin_item_height">70.0dip</dimen>
<dimen name="dicover_page_plugin_item_image_height">70.0dip</dimen>
<dimen name="dicover_page_plugin_item_image_width">150.0dip</dimen>
<dimen name="dicover_page_plugin_item_margin_bottom">10.0dip</dimen>
<dimen name="dicover_page_plugin_item_margin_right">12.0dip</dimen>
<dimen name="dicover_page_plugin_item_padding">4.0dip</dimen>
<dimen name="dicover_page_plugin_item_width">150.0dip</dimen>
<dimen name="dicover_page_pullup_enter_delta_slop">50.0dip</dimen>
<dimen name="dicover_page_tab_height">60.0dip</dimen>
<dimen name="dicover_page_title_margin_top">16.0dip</dimen>
<dimen name="dicover_page_title_textsize">14.0dip</dimen>
<dimen name="dicover_page_toolbar_height">50.0dip</dimen>
```

第一部分，查找关键字dicover和main找到发现页相关的尺寸调整，修改发现页的字体大小和图标大小。

```xml
<dimen name="launcher_widget_delete_button_offset">3.0dip</dimen>
<dimen name="launcher_widget_height_portrait">76.0dip</dimen>
<dimen name="launcher_widget_icon_margin_top_portrait">10.0dip</dimen>
<dimen name="launcher_widget_iconview_height_portrait">40.0dip</dimen>
<dimen name="launcher_widget_iconview_width_portrait">40.0dip</dimen>
<dimen name="launcher_widget_paddingbottom">0.0dip</dimen>
<dimen name="launcher_widget_paddingleft">0.0dip</dimen>
<dimen name="launcher_widget_paddingright">0.0dip</dimen>
<dimen name="launcher_widget_paddingtop">0.0dip</dimen>
<dimen name="launcher_widget_title_margin_bottom_portrait">0.0dip</dimen>
<dimen name="launcher_widget_title_margin_top_portrait">7.0dip</dimen>
<dimen name="launcher_widget_title_padding_x">4.0dip</dimen>
<dimen name="launcher_widget_title_textsize_portrait">11.0dip</dimen>
<dimen name="launcher_widget_width_portrait">56.599976dip</dimen>
```

第二部分，查找关于插件的相关代码，修改插件的尺寸和图标大小

```xml
<dimen name="main_menu_guide_tip_arrow_margin_top">9.0dip</dimen>
<dimen name="main_setting_dot_size_margin_left">4.0dip</dimen>
<dimen name="main_setting_view_item_height">60.0dip</dimen>
<dimen name="mainmenu_bg_radius">20.0dip</dimen>
<dimen name="mainmenu_content_height">258.0dip</dimen>
<dimen name="mainmenu_content_padding">14.0dip</dimen>
<dimen name="mainmenu_firstrow_margin_top">90.0dip</dimen>
<dimen name="mainmenu_item_icon_size">30.0dip</dimen>
<dimen name="mainmenu_item_icon_tips_size">5.0dip</dimen>
<dimen name="mainmenu_item_text_margin_top">8.0dip</dimen>
<dimen name="mainmenu_item_text_size">10.0dip</dimen>
<dimen name="mainmenu_left_image_width">40.0dip</dimen>
<dimen name="mainmenu_left_lable_maxwidth">200.0dip</dimen>
<dimen name="mainmenu_leftview_margin_right">15.0dip</dimen>
<dimen name="mainmenu_leftview_margin_top">30.0dip</dimen>
<dimen name="mainmenu_margin_bottom">10.0dip</dimen>
<dimen name="mainmenu_margin_x">10.0dip</dimen>
<dimen name="mainmenu_row_height">74.0dip</dimen>
<dimen name="media_menu_bottom_margin">2.0dip</dimen>
```

第三部分，查找菜单的相关代码，修改main里的menu菜单的尺寸，找到与登陆相关的代码修改为负值，找到上下菜单边距的缺省值和填充值进行自定义

```xml
<dimen name="user_feedback_bbs_tip_textsize">13.0dip</dimen>
<dimen name="user_feedback_contact_input_box_height">33.0dip</dimen>
<dimen name="user_feedback_content_input_box_height">150.0dip</dimen>
<dimen name="user_feedback_content_input_box_margin_bottom">16.0dip</dimen>
<dimen name="user_feedback_content_input_box_margin_top">20.0dip</dimen>
<dimen name="user_feedback_content_input_box_margin_x">30.0dip</dimen>
<dimen name="user_feedback_content_input_box_padding_x">14.0dip</dimen>
<dimen name="user_feedback_content_input_box_padding_y">12.0dip</dimen>
<dimen name="user_feedback_content_textsize">16.0dip</dimen>
```

第四部分，修改feedback的相关文字和尺寸

```xml
<dimen name="clound_sync_allow_tip_margin_top">80.0dip</dimen>
<dimen name="clound_sync_allow_tip_textsize">10.0dip</dimen>
<dimen name="clound_sync_center_login_item_icon_margin_bottom">16.0dip</dimen>
<dimen name="clound_sync_center_login_item_name_textsize">12.0dip</dimen>
<dimen name="clound_sync_center_qq_login_margin_right">54.0dip</dimen>
<dimen name="clound_sync_content_icon_padding">6.0dip</dimen>
<dimen name="clound_sync_edit_under_line_height">1.0dip</dimen>
<dimen name="clound_sync_edit_under_line_select_height">1.0dip</dimen>
<dimen name="clound_sync_edittext_text_size">16.0dip</dimen>
<dimen name="clound_sync_edittext_width">230.0dip</dimen>
<dimen name="clound_sync_exit_account_margin_right">10.0dip</dimen>
<dimen name="clound_sync_exit_container_margin_bottom">24.0dip</dimen>
<dimen name="clound_sync_exit_container_margin_top">20.0dip</dimen>
<dimen name="clound_sync_import_btn_height">30.0dip</dimen>
<dimen name="clound_sync_import_btn_width">187.0dip</dimen>
<dimen name="clound_sync_item_arrow_margin_right">16.0dip</dimen>
<dimen name="clound_sync_item_arrow_size">22.0dip</dimen>
<dimen name="clound_sync_item_desc_text_size">14.0dip</dimen>
<dimen name="clound_sync_item_import_padding_bottom">14.0dip</dimen>
<dimen name="clound_sync_item_import_padding_top">14.0dip</dimen>
<dimen name="clound_sync_item_import_text_size">12.0dip</dimen>
<dimen name="clound_sync_item_margin_inner_right">10.0dip</dimen>
<dimen name="clound_sync_item_margin_left">24.0dip</dimen>
<dimen name="clound_sync_item_padding_bottom">23.0dip</dimen>
<dimen name="clound_sync_item_padding_top">23.0dip</dimen>
<dimen name="clound_sync_item_text_size">14.0dip</dimen>
<dimen name="clound_sync_login_btn_height">50.0dip</dimen>
<dimen name="clound_sync_login_btn_text_size">14.0dip</dimen>
<dimen name="clound_sync_login_btn_width">156.0dip</dimen>
<dimen name="clound_sync_login_shape_radius">25.0dip</dimen>
<dimen name="clound_sync_logo_height">87.0dip</dimen>
<dimen name="clound_sync_logo_margin_top">88.0dip</dimen>
<dimen name="clound_sync_logo_width">138.0dip</dimen>
<dimen name="clound_sync_margin_logo_top">88.0dip</dimen>
<dimen name="clound_sync_margin_logo_top_min">60.0dip</dimen>
<dimen name="clound_sync_now_text_size">14.0dip</dimen>
<dimen name="clound_sync_other_way_line_height">1.0px</dimen>
<dimen name="clound_sync_other_way_line_width">48.0dip</dimen>
<dimen name="clound_sync_other_way_margin">62.0dip</dimen>
<dimen name="clound_sync_other_way_phone_margin">42.0dip</dimen>
<dimen name="clound_sync_other_way_text_margin_bottom">32.0dip</dimen>
<dimen name="clound_sync_other_way_text_margin_left">32.0dip</dimen>
<dimen name="clound_sync_other_way_text_margin_right">32.0dip</dimen>
<dimen name="clound_sync_other_way_text_margin_top">24.0dip</dimen>
<dimen name="clound_sync_other_way_text_size">10.0dip</dimen>
<dimen name="clound_sync_phone_number_margin_left">60.0dip</dimen>
<dimen name="clound_sync_phone_number_margin_right">60.0dip</dimen>
<dimen name="clound_sync_recent_text_size">10.0dip</dimen>
<dimen name="clound_sync_sync_btn_container_margin_top">34.0dip</dimen>
<dimen name="clound_sync_sync_btn_height">50.0dip</dimen>
<dimen name="clound_sync_sync_btn_width">152.0dip</dimen>
<dimen name="clound_sync_verif_code_stroke">1.0px</dimen>
<dimen name="clound_sync_verif_code_text_height">30.0dip</dimen>
<dimen name="clound_sync_verif_code_text_size">14.0dip</dimen>
<dimen name="clound_sync_verif_code_text_width">110.0dip</dimen>
```

第五部分，找到云同步相关的代码，修改文字和云同步的界面，我直接选择去掉了同步界面 3.进阶修改class文件 打开反编译后文件夹里的class.dex文件使用dex查看器打开，修改里面的升级更新相关代码