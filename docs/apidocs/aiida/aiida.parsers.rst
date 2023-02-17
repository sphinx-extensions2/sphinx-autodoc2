:py:mod:`aiida.parsers`
=======================

.. py:module:: aiida.parsers


Description
-----------

Module for classes and utilities to write parsers for calculation jobs.

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Parser <aiida.parsers.parser.Parser>`
     - Base class for a Parser that can parse the outputs produced by a CalcJob process.

API
~~~

.. py:class:: Parser(node: aiida.orm.CalcJobNode)
   :canonical: aiida.parsers.parser.Parser

   Bases: :py:obj:`abc.ABC`

   Base class for a Parser that can parse the outputs produced by a CalcJob process.

   .. py:method:: __init__(node: aiida.orm.CalcJobNode)
      :canonical: aiida.parsers.parser.Parser.__init__

      Construct the Parser instance.

      :param node: the `CalcJobNode` that contains the results of the executed `CalcJob` process.


   .. py:property:: logger
      :canonical: aiida.parsers.parser.Parser.logger

      Return the logger preconfigured for the calculation node associated with this parser instance.

      :return: `logging.Logger`


   .. py:property:: node
      :canonical: aiida.parsers.parser.Parser.node
      :type: aiida.orm.CalcJobNode

      Return the node instance

      :return: the `CalcJobNode` instance


   .. py:property:: exit_codes
      :canonical: aiida.parsers.parser.Parser.exit_codes
      :type: aiida.engine.ExitCodesNamespace

      Return the exit codes defined for the process class of the node being parsed.

      :returns: ExitCodesNamespace of ExitCode named tuples


   .. py:property:: retrieved
      :canonical: aiida.parsers.parser.Parser.retrieved
      :type: aiida.orm.FolderData

   .. py:property:: outputs
      :canonical: aiida.parsers.parser.Parser.outputs

      Return the dictionary of outputs that have been registered.

      :return: an AttributeDict instance with the registered output nodes


   .. py:method:: out(link_label: str, node: aiida.orm.Data) -> None
      :canonical: aiida.parsers.parser.Parser.out

      Register a node as an output with the given link label.

      :param link_label: the name of the link label
      :param node: the node to register as an output
      :raises aiida.common.ModificationNotAllowed: if an output node was already registered with the same link label


   .. py:method:: get_outputs_for_parsing()
      :canonical: aiida.parsers.parser.Parser.get_outputs_for_parsing

      Return the dictionary of nodes that should be passed to the `Parser.parse` call.

      Output nodes can be marked as being required by the `parse` method, by setting the `pass_to_parser` attribute,
      in the `spec.output` call in the process spec of the `CalcJob`, to True.

      :return: dictionary of nodes that are required by the `parse` method


   .. py:method:: parse_from_node(node: aiida.orm.CalcJobNode, store_provenance=True, retrieved_temporary_folder=None) -> typing.Tuple[typing.Optional[typing.Dict[str, typing.Any]], aiida.orm.CalcFunctionNode]
      :canonical: aiida.parsers.parser.Parser.parse_from_node
      :classmethod:

      Parse the outputs directly from the `CalcJobNode`.

      If `store_provenance` is set to False, a `CalcFunctionNode` will still be generated, but it will not be stored.
      It's storing method will also be disabled, making it impossible to store, because storing it afterwards would
      not have the expected effect, as the outputs it produced will not be stored with it.

      This method is useful to test parsing in unit tests where a `CalcJobNode` can be mocked without actually having
      to run a `CalcJob`. It can also be useful to actually re-perform the parsing of a completed `CalcJob` with a
      different parser.

      :param node: a `CalcJobNode` instance
      :param store_provenance: bool, if True will store the parsing as a `CalcFunctionNode` in the provenance
      :param retrieved_temporary_folder: absolute path to folder with contents of `retrieved_temporary_list`
      :return: a tuple of the parsed results and the `CalcFunctionNode` representing the process of parsing


   .. py:method:: parse(**kwargs) -> typing.Optional[aiida.engine.ExitCode]
      :canonical: aiida.parsers.parser.Parser.parse
      :abstractmethod:

      Parse the contents of the output files retrieved in the `FolderData`.

      This method should be implemented in the sub class. Outputs can be registered through the `out` method.
      After the `parse` call finishes, the runner will automatically link them up to the underlying `CalcJobNode`.

      :param kwargs: output nodes attached to the `CalcJobNode` of the parser instance.
      :return: an instance of ExitCode or None

