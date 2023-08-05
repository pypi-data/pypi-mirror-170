###############################################################################
#
# This MobilityDB code is provided under The PostgreSQL License.
#
# Copyright (c) 2019-2022, Université libre de Bruxelles and MobilityDB
# contributors
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose, without fee, and without a written 
# agreement is hereby granted, provided that the above copyright notice and
# this paragraph and the following two paragraphs appear in all copies.
#
# IN NO EVENT SHALL UNIVERSITE LIBRE DE BRUXELLES BE LIABLE TO ANY PARTY FOR
# DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING
# LOST PROFITS, ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION,
# EVEN IF UNIVERSITE LIBRE DE BRUXELLES HAS BEEN ADVISED OF THE POSSIBILITY 
# OF SUCH DAMAGE.
#
# UNIVERSITE LIBRE DE BRUXELLES SPECIFICALLY DISCLAIMS ANY WARRANTIES, 
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS FOR A PARTICULAR PURPOSE. THE SOFTWARE PROVIDED HEREUNDER IS ON
# AN "AS IS" BASIS, AND UNIVERSITE LIBRE DE BRUXELLES HAS NO OBLIGATIONS TO 
# PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS. 
#
###############################################################################
from abc import ABC
from datetime import datetime
from typing import Optional, Union, List

from dateutil.parser import parse
from pymeos_cffi import tint_value_split
from pymeos_cffi.functions import tint_in, tint_out, tintinst_make, \
    datetime_to_timestamptz, tint_values, tint_start_value, \
    tint_end_value, tint_value_at_timestamp
from spans.types import intrange

from .tnumber import TNumber
from ..temporal import TInterpolation, Temporal, TInstant, TSequence, TSequenceSet


class TInt(TNumber, ABC):
    """
    Abstract class for representing temporal integers of any subtype.
    """

    BaseClass = int
    BaseClassDiscrete = True
    _parse_function = tint_in

    @staticmethod
    def read_from_cursor(value, cursor=None):
        if not value:
            return None
        if value[0] != '{' and value[0] != '[' and value[0] != '(':
            return TIntInst(string=value)
        elif value[0] == '[' or value[0] == '(':
            return TIntSeq(string=value)
        elif value[0] == '{':
            if value[1] == '[' or value[1] == '(':
                return TIntSeqSet(string=value)
            else:
                return TIntSeq(string=value)
        raise Exception("ERROR: Could not parse temporal integer value")

    @property
    def value_range(self):
        """
        Range of values taken by the temporal value as defined by its minimum and maximum value
        """
        return intrange(self.min_value, self.max_value, True, True)

    @property
    def start_value(self):
        """
        Start value.
        """
        return tint_start_value(self._inner)

    @property
    def end_value(self):
        """
        End value.
        """
        return tint_end_value(self._inner)

    @property
    def values(self):
        """
        List of distinct values.
        """
        values, count = tint_values(self._inner)
        return [values[i] for i in range(count)]

    def value_at_timestamp(self, timestamp):
        """
        Value at timestamp.
        """
        return tint_value_at_timestamp(self._inner, datetime_to_timestamptz(timestamp), True)

    def value_split(self, start: int, size: int, count: int) -> List[Temporal]:
        tiles, buckets, new_count = tint_value_split(self._inner, start, size, count)
        from ..factory import _TemporalFactory
        return [_TemporalFactory.create_temporal(tiles[i]) for i in range(new_count)]

    @property
    def interpolation(self):
        """
        Interpolation of the temporal value, that is, ``'Stepwise'``.
        """
        return TInterpolation.STEPWISE

    def __str__(self):
        return tint_out(self._inner)

    def as_wkt(self):
        return tint_out(self._inner)


class TIntInst(TInstant, TInt):
    """
    Class for representing temporal integers of instant subtype.

    ``TIntInst`` objects can be created with a single argument of type string
    as in MobilityDB.

        >>> TIntInst(string='10@2019-09-01')

    Another possibility is to give the ``value`` and the ``time`` arguments,
    which can be instances of ``str`` or ``int`` and ``str`` or ``datetime`` respectively.

        >>> TIntInst(value='10', timestamp='2019-09-08 00:00:00+01')
        >>> TIntInst(value=10, timestamp=parse('2019-09-08 00:00:00+01'))

    """

    _make_function = tintinst_make
    _cast_function = int

    def __init__(self, string: Optional[str] = None, *, value: Optional[Union[str, int]] = None,
                 timestamp: Optional[Union[str, datetime]] = None, _inner=None):
        super().__init__(string=string, value=value, timestamp=timestamp, _inner=_inner)


class TIntSeq(TSequence, TInt):
    """
    Class for representing temporal integers of sequence subtype.

    ``TIntSeq`` objects can be created with a single argument of type string
    as in MobilityDB.

        >>> TIntSeq('[10@2019-09-01 00:00:00+01, 20@2019-09-02 00:00:00+01, 10@2019-09-03 00:00:00+01]')

    Another possibility is to give the arguments as follows:

    * ``instantList`` is the list of composing instants, which can be instances of
      ``str`` or ``TIntInst``,
    * ``lower_inc`` and ``upper_inc`` are instances of ``bool`` specifying
      whether the bounds are inclusive or not. By default ``lower_inc``
      is ``True`` and ``upper_inc`` is ``False``.

    Some pymeos_examples are given next.

        >>> TIntSeq(['10@2019-09-01 00:00:00+01', '20@2019-09-02 00:00:00+01', '10@2019-09-03 00:00:00+01'])
        >>> TIntSeq([TIntInst('10@2019-09-01 00:00:00+01'), TIntInst('20@2019-09-02 00:00:00+01'), TIntInst('10@2019-09-03 00:00:00+01')])
        >>> TIntSeq(['10@2019-09-01 00:00:00+01', '20@2019-09-02 00:00:00+01', '10@2019-09-03 00:00:00+01'], True, True)
        >>> TIntSeq([TIntInst('10@2019-09-01 00:00:00+01'), TIntInst('20@2019-09-02 00:00:00+01'), TIntInst('10@2019-09-03 00:00:00+01')], True, True)

    """

    ComponentClass = TIntInst

    def __init__(self, string: Optional[str] = None, *, instant_list: Optional[List[Union[str, TIntInst]]] = None,
                 lower_inc: bool = True, upper_inc: bool = False,
                 interpolation: TInterpolation = TInterpolation.STEPWISE, normalize: bool = True, _inner=None):
        super().__init__(string=string, instant_list=instant_list, lower_inc=lower_inc, upper_inc=upper_inc,
                         interpolation=interpolation, normalize=normalize, _inner=_inner)


class TIntSeqSet(TSequenceSet, TInt):
    """
    Class for representing temporal integers of sequence subtype.

    ``TIntSeqSet`` objects can be created with a single argument of type string
    as in MobilityDB.

        >>> TIntSeqSet('{[10@2019-09-01 00:00:00+01], [20@2019-09-02 00:00:00+01, 10@2019-09-03 00:00:00+01]}')

    Another possibility is to give the list of composing sequences, which
    can be instances of ``str`` or ``TIntSeq``.

        >>> TIntSeqSet(['[10@2019-09-01 00:00:00+01]', '[20@2019-09-02 00:00:00+01, 10@2019-09-03 00:00:00+01]'])
        >>> TIntSeqSet([TIntSeq('[10@2019-09-01 00:00:00+01]'), TIntSeq('[20@2019-09-02 00:00:00+01, 10@2019-09-03 00:00:00+01]')])
        >>> TIntSeqSet([TIntSeq('[10@2019-09-01 00:00:00+01]'), TIntSeq('[20@2019-09-02 00:00:00+01, 10@2019-09-03 00:00:00+01]')])

    """

    ComponentClass = TIntSeq

    def __init__(self, string: Optional[str] = None, *, sequence_list: Optional[List[Union[str, TIntSeq]]] = None,
                 normalize: bool = True, _inner=None):
        super().__init__(string=string, sequence_list=sequence_list, normalize=normalize, _inner=_inner)
