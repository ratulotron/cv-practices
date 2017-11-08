# Train new font
PANGOCAIRO_BACKEND=fc text2image --text=training_text.txt --outputbase=circle.zap.exp0 --font='DejaVu Sans' --fonts_dir=.

tesseract circle.zap.exp0.tif circle.zap.exp0 box.train.stderr

# mftraining
mftraining -F font_properties -U unicharset -O circle.unicharset circle.zap.exp0.tr circle.zap.exp1.tr

# cntraining
cntraining circle.zap.exp0.tr circle.zap.exp1.tr