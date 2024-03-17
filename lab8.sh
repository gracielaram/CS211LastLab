#!/bin/bash
python3 $1
grep -n 'class\|App\|import\|greeting\|1\|main\|def\|275x250' $1

