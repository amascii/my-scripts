#!/bin/bash
for file in *.jfif; do convert "$file" "${file%.jfif}.jpg"; done
