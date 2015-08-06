#!/usr/bin/env sh

TOOLS=./build/tools

$TOOLS/caffe train \
  --solver=models/bvlc_googlenet/jd_solver.prototxt

$TOOLS/caffe train \
  --solver=models/bvlc_googlenet/jd_solver.prototxt
  --snapshot=models/bvlc/googlenet/jd_googlenet_quick_iter_8000.solverstate
