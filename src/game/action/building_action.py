"""Module to handle building actions."""

def CheckState(states):
  def CheckStateDecorator(function):
    # pylint: disable=W0212
    def FunctionWithStateCheck(self, *args, **kwargs):
      if self._state not in states:
        raise BuildingActionError(
            'Action state %s not among %s' % (self._state, states))
      return function(self, *args, **kwargs)
    return FunctionWithStateCheck
  return CheckStateDecorator

class BuildingActionError(Exception):
  pass

class ActionStates(object):
  PENDING_START_ACTION = 'State: pending start action'
  PENDING_TRANSACTION = 'State: pending transaction'
  PENDING_SECOND_TRANSACTION = 'State: pending the second transaction'
  DONE = 'State: done'


class BuildingAction(object):
  def __init__(self, player_obj, need_selection=False, two_transactions=False):
    self._player = player_obj
    self._need_selection = need_selection
    self._two_transactions = two_transactions
    self._state = ActionStates.PENDING_START_ACTION

  @CheckState([ActionStates.PENDING_START_ACTION])
  def StartAction(self):
    # Simple action which does not need user selection is handled here.
    self._SimpleActionImpl()

    # Returns a picker for action that needs selection.
    if self._need_selection:
      picker = self._CreatePickerImpl()
      self._state = ActionStates.PENDING_TRANSACTION 
      return picker

    self._state = ActionStates.DONE
    return None

  # Subclass optionally implements these functions.
  def _CreatePickerImpl(self):
    """Creates a picker for user to select something.

    There are these examples:
    1. User selects resources to transform.
    2. User selects building to build.
    3. User selects ships and resources to ship.
    """
    pass

  def _ClearPickerImpl(self):
    """Clears picker to prepare for the second transaction."""
    pass

  def _TransactionImpl(self):
    """Transaction after picker.Pick is done by user."""
    pass

  def _SimpleActionImpl(self):
    """Simple action that does not need user selection."""
    pass

  @CheckState([ActionStates.PENDING_TRANSACTION,
               ActionStates.PENDING_SECOND_TRANSACTION])
  def Transaction(self):
    # Transaction which needs user selection is handled here.
    self._TransactionImpl()

    self._ClearPickerImpl()

    if self._state == ActionStates.PENDING_SECOND_TRANSACTION:
      self._state = ActionStates.DONE
      return

    if self._two_transactions:
      self._state = ActionStates.PENDING_SECOND_TRANSACTION
      return

    self._state = ActionStates.DONE

  @CheckState([ActionStates.PENDING_SECOND_TRANSACTION])
  def EndAction(self):
    self._state = ActionStates.DONE

  def IsDone(self):
    return self._state == ActionStates.DONE
