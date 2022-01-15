# ------------------------------------------------------------------------------
# Purpose:       musicdiff is a package for comparing music scores using music21.
#
# Authors:       Greg Chapman <gregc@mac.com>
#                musicdiff is derived from:
#                   https://github.com/fosfrancesco/music-score-diff.git
#                   by Francesco Foscarin <foscarin.francesco@gmail.com>
#
# Copyright:     (c) 2022 Francesco Foscarin, Greg Chapman
# License:       MIT, see LICENSE
# ------------------------------------------------------------------------------

__all__ = [
]

import sys
import os
from typing import Union, List, Tuple
from pathlib import Path

import music21 as m21

from musicdiff.m21utils import M21Utils
from musicdiff.annotation import AnnScore
from musicdiff.comparison import Comparison
from musicdiff.visualization import Visualization

def _getInputExtensionsList() -> [str]:
    c = m21.converter.Converter()
    inList = c.subconvertersList('input')
    result = []
    for subc in inList:
        for inputExt in subc.registerInputExtensions:
            result.append('.' + inputExt)
    return result

def _printSupportedInputFormats():
    c = m21.converter.Converter()
    inList = c.subconvertersList('input')
    print("Supported input formats are:", file=sys.stderr)
    for subc in inList:
        if subc.registerInputExtensions:
            print('\tformats   : ' + ', '.join(subc.registerFormats)
                    + '\textensions: ' + ', '.join(subc.registerInputExtensions), file=sys.stderr)

def diff(score1: Union[str, Path, m21.stream.Score], # can be file or Score
         score2: Union[str, Path, m21.stream.Score], # can be file or Score
         force_parse: bool = True, # should we force music21 to re-parse a file it has parsed recently?
         visualize_diffs: bool = True, # should we display the scores with differences marked?
        ) -> int: # returns numDiffs.  0 means scores were identical, None means the diff failed.

    badArg1: bool = False
    badArg2: bool = False
    if isinstance(score1, (str, Path)):
        file1 = score1
        _, fileExt1 = os.path.splitext(file1)

        if fileExt1 not in _getInputExtensionsList():
            print(f'score1 file extension "{fileExt1}"" not supported.', file=sys.stderr)
            badArg1 = True

        if not badArg1:
            try:
                score1 = m21.converter.parse(file1, forceSource = force_parse)
            except:
                print(f'score1 ({file1}) could not be parsed by music21', file=sys.stderr)
                badArg1 = True

    if isinstance(score2, (str, Path)):
        file2 = score2
        _, fileExt2 = os.path.splitext(file2)

        if fileExt2 not in _getInputExtensionsList():
            print(f'score2 file extension "{fileExt2}"" not supported.', file=sys.stderr)
            badArg2 = True

        if not badArg2:
            try:
                score2 = m21.converter.parse(file2, forceSource = force_parse)
            except:
                print(f'score2 ({file2}) could not be parsed by music21', file=sys.stderr)
                badArg2 = True

    if badArg1 or badArg2:
        return None

    # scan each score, producing an annotated wrapper
    annotated_score1: AnnScore = AnnScore(score1)
    annotated_score2: AnnScore = AnnScore(score2)

    diff_list: List = None
    _cost: int = None
    diff_list, _cost = Comparison.annotated_scores_diff(annotated_score1, annotated_score2)

    numDiffs: int = len(diff_list)
    if visualize_diffs and numDiffs != 0:
        # you can change these three colors as you like...
        #Visualization.INSERTED_COLOR = 'red'
        #Visualization.DELETED_COLOR = 'red'
        #Visualization.CHANGED_COLOR = 'red'

        # color changed/deleted/inserted notes, add descriptive text for each change, etc
        Visualization.mark_diffs(score1, score2, diff_list)

        # ask music21 to display the scores as PDFs.  Composer's name will be prepended with
        # 'score1 ' and 'score2 ', respectively, so you can see which is which.
        Visualization.show_diffs(score1, score2)

    return numDiffs
