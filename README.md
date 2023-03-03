# ☁ Cloud Creation ☁

## About This

**Discord bot** made with Cloudinary that able to edit your images on the fly, with capabilities to generate from local files by drag'n'drop, using this tool you can get inmediately results

## Edit Your Avatar Profile Picture

By accessing to the user Avatar, this action is called with the next command in the Discord chat input:

```
/av member: @username: discord.Member
```

Where **/av** is the call to action **member=** is the param, **@username** is the username of a Discord member and ==discord.Member== is the Type of Data it's support

Its recover your avatar and then we can transform it on the fly with many options:

- [x] [Sepia](#sepia-effect)
- [x] [Color Silhouette](#color-silhouette)
- [x] [Whitify](#whitify)
- [x] [Black'n'White](#blacknwhite)
- [x] [High_Contrast](#high-contrast)
- [x] [Colorful](#colorful)

Any interaction Have the form drag'n'drop [^7] option with any command You call with the specific argument

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

Where **/color_silhouette** is the call to action **drag** is the file form directory or clipboard, **color** have variety options where you can choice what te color you want to transform the picture, and **description** is a little words to describe the image, _this param is optional_

example of color choice:

<image src='https://cdn.discordapp.com/attachments/886862316509999114/1081263798779924520/image.png' />

And a quick example of the results where we drop this image:

<image src='https://res.cloudinary.com/diegato/image/upload/v1/Bot/9dc35c25870a23b2020446d5ef76c94b.png.png'>

#### And with the Pink Choice we obtain:

<image src='https://res.cloudinary.com/diegato/image/upload/e_blackwhite:50/co_rgb:D867B4,e_colorize:50/e_brightness:30/v1/Bot/9dc35c25870a23b2020446d5ef76c94b.png.png'>

## Whitify

This feature use Drag'n'drop to upload files in the input of the Discord chat, the command to the action is:

```
/whitify drag: FileAttachment, description: str | None
```

Where **/whitify** is the call to action **drag** is the file form directory or clipboard and **description** is a little words to describe the image, _this param is optional_

Effect: This effect lowered the color and saturation and give a white bright light to the skin and the enviroment.

Example Result:

<image src='https://images-ext-2.discordapp.net/external/izyW6gMMuthnYASMV8XSjUZGWAk1SlJhdTSLiE718lM/https/res.cloudinary.com/diegato/image/upload/e_contrast%3A50/e_saturation%3A-40/v1/Bot/f.png.png?width=901&height=676'>

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
