#!/usr/bin/env bash

INPUT_AUDIO="whisper-input-videos/000-gente-rota_calor_y_mas_calor/000-gente_rota_-_calor_y_mas_calor.mp4"
OUTPUT_DIR="output"
LANGUAGE_CODES="es pt hr en"
MODEL="tiny"

for LANGUAGE_CODE in $LANGUAGE_CODES; do
  RESULT="$OUTPUT_DIR/$LANGUAGE_CODE.txt"
  whisper --model "$MODEL" --task translate --language "$LANGUAGE_CODE" --audio "$INPUT_AUDIO" --output "$RESULT" &
done
wait
