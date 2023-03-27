# ☁ Cloud Creation ☁

---

## About This

**Discord bot** made with Cloudinary that able to edit your images on the fly, with capabilities to generate from local files by drag'n'drop, using this tool you can get inmediately results

## Edit Your Avatar Profile Picture

By accessing to the user Avatar, this action is called with the next command in the Discord chat input:

```
/av member: @username: discord.Member
```

## Index

#### - Avatar

#### - [Sepia](#sepia-effect)

#### - [Color Silhouette](#color-silhouette-1)

#### - [Two Color Silhouette](#two-color-silhouette-1)

#### - [Whitify](#whitify-1)

#### - [Black'n'White](#blacknwhite-1)

#### - [High_Contrast](#high-contrast)

#### - [Colorful](#colorful-1)

#### - [Background Remove](#background-remove-1)

#### - [Cartoonify](#cartoonify-1)

#### - [Error Handling](#error-handling-1)

---

Where **/av** is the call to action **member=** is the param, **@username** is the username of a Discord member and ==discord.Member== is the Type of Data it's support

Its recover your avatar and then we can transform it on the fly with many options:

- [x] [Sepia](#sepia-effect)
- [x] [Color Silhouette](#color-silhouette)
- [x] [Whitify](#whitify)
- [x] [Black'n'White](#blacknwhite)
- [x] [High_Contrast](#high-contrast)
- [x] [Colorful](#colorful)

Any interaction Have the form drag'n'drop [^1] option with any command You call with the specific argument

### Important!!!

_The name of the user you want to access need to be with ==natural characters== and words, cloudinary don't support special char in the name that its used for store the image for a while during the transformation is made_

Example with my discord username =="𝕯𝖎𝖊𝖌𝖆𝖙𝖔#4880"==, since its contain special chars, cloudinary service denied the access to save the files and throw ExceptionError like the image below:

<image src="https://cdn.discordapp.com/attachments/1075776011209277510/1080865285365579877/image.png" />

## Sepia Effect

This feature use Drag'n'drop to upload files in the input of the Discord chat, the command to the action is:

```
/sepia_effect drag: FileAttachment, description: str | None
```

Where **/sepia_effect** is the call to action **drag** is the file form directory or clipboard and **description** is a little words to describe the image, _this param is optional_

Example Result:

<image src='https://res.cloudinary.com/diegato/image/upload/e_sepia/v1/Bot/UnChinoMasq:av_up' />

## Color Silhouette

This feature use Drag'n'drop to upload files in the input of the Discord chat, the command to the action is:

```
/color_silhouette drag: FileAttachment, color: Options.Color[🟥,🟧,🟨,🟩,🟦,🟪,] [max=1] , description: str | None
```

Where **/color_silhouette** is the call to action **drag** is the file form directory or clipboard, **color** have variety options where you can choice what the color you want to transform the picture, and **description** is a little words to describe the image, _this param is optional_

example of color choice:

<image src='https://cdn.discordapp.com/attachments/886862316509999114/1081263798779924520/image.png' />

And a quick example of the results where we drop this image:

<image height='720px' src='https://res.cloudinary.com/diegato/image/upload/v1/Bot/9dc35c25870a23b2020446d5ef76c94b.png.png'>

#### And with the Pink Choice we obtain:

<image height='720px' src='https://res.cloudinary.com/diegato/image/upload/e_blackwhite:50/co_rgb:D867B4,e_colorize:50/e_brightness:30/v1/Bot/9dc35c25870a23b2020446d5ef76c94b.png.png'>

## Two Color Silhouette

This feature use Drag'n'drop to upload files in the input of the Discord chat, the command to the action is:

```
/color_silhouette drag: FileAttachment, color: Options.Color[🟥,🟧,🟨,🟩,🟦,🟪,] [max=2] , description: str | None
```

Where **/two_color_silhouette** is the call to action **drag** is the file form directory or clipboard, **color** have variety options where you can choice what the color you want to transform the picture, the first color will be set in the left place and the second in the right place, and **description** is a little words to describe the image, _this param is optional_

Example:

<image src='https://images-ext-1.discordapp.net/external/fgUtq9LswX86j1t-JXYRpxxkvV2adRLFJ636CotW4K4/https/res.cloudinary.com/diegato/image/upload/c_crop%2Cg_west%2Ch_1.0%2Cw_0.5/e_blackwhite%3A39/co_rgb%3A09f%2Ce_colorize%3A50/e_brightness%3A30/l_Bot%3A20225251631678_1.jpg.png/c_crop%2Cg_east%2Ch_1.0%2Cw_0.5/e_blackwhite%3A39/co_rgb%3ACF2C2C%2Ce_colorize%3A30/e_brightness%3A29/fl_layer_apply%2Cg_east%2Cx_-600.0/v1/Bot/20225251631678_1.jpg.png' />

## Whitify

This feature use Drag'n'drop to upload files in the input of the Discord chat, the command to the action is:

```
/whitify drag: FileAttachment, description: str | None
```

Where **/whitify** is the call to action **drag** is the file form directory or clipboard and **description** is a little words to describe the image, _this param is optional_

Effect: This effect lowered the color and saturation and give a white bright light to the skin and the enviroment.

## Black'n'White

This feature use Drag'n'drop to upload files in the input of the Discord chat, the command to the action is:

```
/black_and_white drag: FileAttachment, description: str | None
```

Where **/black_and_white** is the call to action **drag** is the file form directory or clipboard and **description** is a little words to describe the image, _this param is optional_

Example Result:

<image src='https://res.cloudinary.com/diegato/image/upload/e_grayscale/v1/Bot/mission_complete_logo.png.png' />

## High Contrast

This feature use Drag'n'drop to upload files in the input of the Discord chat, the command to the action is:

```
/high_contrast drag: FileAttachment, description: str | None
```

Where **/high_contrast** is the call to action **drag** is the file form directory or clipboard and **description** is a little words to describe the image, _this param is optional_

## Colorful

This feature use Drag'n'drop to upload files in the input of the Discord chat, the command to the action is:

```
/colorful drag: FileAttachment, description: str | None
```

Where **/colorful** is the call to action **drag** is the file form directory or clipboard and **description** is a little words to describe the image, _this param is optional_

## Layout Of

This feature use 2 Drag'n'drop, you might to upload in the first drag the **desire** profile picture and in the second drag yout **desire** Banner.

<image src='https://cdn.discordapp.com/attachments/886862316509999114/1081603556257300561/image.png' />

call to action:

```
/layout_of drag_pfp: FileAttachment, drag_banner: FileAttachment
```

After the call to action you can set the option of the social media you want to see the result by clicking in any button:

<image src='https://cdn.discordapp.com/attachments/886862316509999114/1081604611166707712/image.png' />

### Result:

<image src='https://res.cloudinary.com/diegato/image/upload/c_thumb,g_auto,h_315,w_851/l_UsersLayout:Diegato_av/c_thumb,g_auto:face,h_120,w_120,z_0.5/r_max/fl_layer_apply,g_south_west,x_20,y_11/l_Layouts:facebook-layout/c_thumb,g_south,h_315,w_851/fl_layer_apply,g_south/v1/UsersLayout/Diegato_banner' />

<image src='https://cdn.discordapp.com/attachments/886862316509999114/1081605841154744320/image.png' />

By clicking in the Download Button, You will see the Image With the size perfectly for the social media, for avatar and for banner individually

## Cartoonify

This feature use Drag'n'drop to upload files in the input of the Discord chat, the command to the action is:

```
/cartoonify drag: FileAttachment, description: str | None
```

Where **/cartoonify** is the call to action **drag** is the file form directory or clipboard and **description** is a little words to describe the image, _this param is optional_

#### Example:

<image src="https://res.cloudinary.com/diegato/image/upload/e_cartoonify/v1/Bot/miduNoBg.png.png" />

## Background Remove

---

- This feature have an issue related to the response time of Discord and with the generation image of cloudinary, since the image take 30s or more to generate but Discord cancel the response after trying to get the data in 3 seconds, this action might not render the image with the removed background in the Discord chat, Also you have the button to download the result of the image that will force the load of it and shown in the browser to download. [see more](#remove-background-image-dont-render).

call to action:

```
/background_removal drag: FileAttachment, description: str | None
```

Simple: from a normal image it will transform and with AI remove those that consider "background"

Complex: This action is heavy to make, so the content may late a bit to render but with the link you can shown the result in the browser.

## Texturize!

---

You can apply a curious effect by using the command /texturize, this command will convert your image to be like in some plain areas like a wall, underwater or in cobblestones!

call to action:

```
/texturize drag: Fileattachment, strength: Choice[int], effect: Choice[str]
```

Example of the result:

<image src='https://media.licdn.com/dms/image/C4D22AQFDD8T4bVpdbA/feedshare-shrink_1280/0/1678220895528?e=1681344000&v=beta&t=jiAdYCwxlrENihCXxW-rT8JNjGHktrWcdK7W5TLrCKY' />

---

## Error Handling

---

Sometimes When you call an action with the slash command, may throw an error application don't response

<image src="https://cdn.discordapp.com/attachments/886862316509999114/1081608713820962857/image.png" />

This might happen for Some reason:

**1.- Connection error with the platform**

**2.- Discord TimeOut (tried more than 3 seconds to call the command)**

**3.- Internet too Slow**

**4.- I Hate You (jk)**

**5.- Cloudinary Service Might be Down for a while**

There's not a directly solution for this error, just only retry to use the command in a few seconds

### Remove Background image don't render

---

The estimated result looks like:

<image src='https://media.discordapp.net/attachments/886862316509999114/1081612733063114823/image.png' />

But sometimes you wouldn't see the image instantly, so you can try to reload the image in 30 seconds by clicking again the "load Btn"

or trying to download directly with the "Download Button" and its will redirect to the browser
