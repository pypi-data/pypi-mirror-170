import * as React from 'react';
import CloseIcon from '@material-ui/icons/Close';
import { IconButton } from '@material-ui/core';
import { Select } from './../components/Select';
import TagsUtils from './../lib/TagsUtils';
import { NotebookPanel } from '@jupyterlab/notebook';
import { Chip, Tooltip } from '@material-ui/core';

const CELL_TYPE_NA = 'na';
const CELL_TYPE_NA_LABEL = '-';
const CELL_TYPES: any[] = [
    {
        value: CELL_TYPE_NA,
        label: CELL_TYPE_NA_LABEL,
        helpText: null,
        chipColor: null 
    },
    {
        value: 'requirements',
        label: 'Requirements',
        helpText: 'The code in this cell will be parsed as requirements packages and install in system.',
        chipColor: 'a32626'
    },
    {
        value: 'preprocessor',
        label: 'Pre processor',
        helpText: 'The code in this cell will be parsed as preprocessor for the predict function of deployed model.',
        chipColor: 'ee7a1a'
    },
    {
        value: 'postprocessor',
        label: 'Post processor',
        helpText: 'The code in this cell will be parsed as postprocessor for the predict function of deployed model.',
        chipColor: '773d0d'
    },
    {
        value: 'functions',
        label: 'Extra functions',
        helpText: 'The code in this cell will be parsed as referenced function for the preprocessor or postprocessor.',
        chipColor: 'a32626'
    }
];

const CELL_TYPE_SELECT_OPTIONS = CELL_TYPES
    .map(item => {
        const newItem = { ...item };
        delete newItem['helpText'];
        delete newItem.chipColor;
        return newItem;
    });

export const RESERVED_CELL_NAMES: string[] = CELL_TYPES
    .filter(item => item['value'] !== CELL_TYPE_NA)
    .map(item => {
        return item['value'];
    });

export const RESERVED_CELL_NAMES_HELP_TEXT = CELL_TYPES
    .reduce((obj, item) => {
        obj[item.value] = item.helpText;
        return obj;
    } ,{});

export const RESERVED_CELL_NAMES_CHIP_COLOR = CELL_TYPES
    .reduce((obj, item) => {
        obj[item.value] = item.chipColor;
        return obj;
    } ,{});

const STEP_NAME_ERROR_MSG = `Step name must consist of lower case alphanumeric characters or \'_\', and can not start with a digit.`;

export interface IProps {
  notebookPanel: NotebookPanel;
  cellElement: any;
  transformerTag?: string;
}

interface IState {
    transformerTag?: string;
    isChipVisible?: boolean;
    isSelectorVisible?: boolean;
    // used to store the closest preceding block name. Used in case the current
    // block name is empty, to suggest merging to the previous one.
    previousStepName?: string;
    stepNameErrorMsg?: string;
    // flag to open the metadata editor dialog dialog
    // XXX (stefano): I would like to set this as required, but the return
    // XXX (stefano): updatePreviousStepName don't allow me.
    cellMetadataEditorDialog?: boolean;
}

/**
 * Component that allow to edit the Kale cell tags of a notebook cell.
 */
export class CellMetadataEditor extends React.Component<IProps, IState> {

  constructor(props: IProps) {
      super(props);
      // We use this element reference in order to move it inside Notebooks's cell
      // element.
      const DefaultState: IState = {
          transformerTag: props.transformerTag?props.transformerTag : null,
          isChipVisible: RESERVED_CELL_NAMES.includes(props.transformerTag)? true: false,
          previousStepName: null,
          stepNameErrorMsg: STEP_NAME_ERROR_MSG,
          cellMetadataEditorDialog: false,
      };
      this.state = DefaultState;
      this.updateCurrentBlockName = this.updateCurrentBlockName.bind(this);
      this.updateCurrentCellTag = this.updateCurrentCellTag.bind(this);
      this.toggleTagsEditorDialog = this.toggleTagsEditorDialog.bind(this);
  }

  componentWillUnmount() {
  }

  updateCurrentCellTag = (value: string) => {
      console.log('updateCurrentCellTag ' + value);
      if (RESERVED_CELL_NAMES.includes(value)) {
          let cellMetadata = {
            transformerTag: value,
          };
          TagsUtils.setCellTransformerTag(
              this.props.notebookPanel,
              this.props.notebookPanel.content.activeCellIndex,
              cellMetadata
          ).then(newValue => {
          });
          this.setState({ transformerTag: value });
      } else if(CELL_TYPE_NA === value) {
          TagsUtils.resetCellTransformerTag(
              this.props.notebookPanel,
              this.props.notebookPanel.content.activeCellIndex,
          ).then(newValue => {
          });
          this.setState({ transformerTag: null });
      }
  };

  isEqual(a: any, b: any): boolean {
    return JSON.stringify(a) === JSON.stringify(b);
  }

  handleEvent(event: Event): void {
    switch (event.type) {
      case 'blur':
        break;
      case 'click':
        break;
      default:
        break;
    }
  }

  componentDidUpdate(prevProps: Readonly<IProps>, prevState: Readonly<IState>) {
    console.log('componentDidUpdate');
    this.hideEditorIfNotCodeCell();
    this.setState(this.updatePreviousStepName);
  }

  hideEditorIfNotCodeCell() {
    console.log('hideEditorIfNotCodeCell');
  }

  updatePreviousStepName(
    state: Readonly<IState>,
    props: Readonly<IProps>,
  ): IState {
    return null;
  }

  updateCurrentBlockName = (value: string) => {
    console.log('updateCurrentBlockName ' + value);
  };

  static getDerivedStateFromProps (props: IProps, state: IState) : any {
    console.log('getDerivedStateFromProps');
    return null;
  }

  /**
   * Function called before updating the value of the block name input text
   * field. It acts as a validator.
   */
  onBeforeUpdate = (value: string) => {
    if (value === this.props.transformerTag) {
      return false;
    }
    this.setState({ stepNameErrorMsg: STEP_NAME_ERROR_MSG });
    return false;
  };

  getPrevStepNotice = () => {
    return this.state.previousStepName && this.props.transformerTag === ''
      ? `Leave the step name empty to merge the cell to step '${this.state.previousStepName}'`
      : null;
  };

  toggleSelector() {
    console.log('toggleSelector');
    if(this.state.isSelectorVisible) {
        this.hideSelector();
    } else {
        this.showSelector();
    }
  }

  showSelector() {
    console.log('showSelector');
    this.setState({
        isSelectorVisible: true,
        isChipVisible: false
    });
  }
  hideSelector() {
    console.log('hideSelector');
    //this.context.onEditorVisibilityChange(false);
    this.setState({
        isSelectorVisible: false,
        isChipVisible: RESERVED_CELL_NAMES.includes(this.state.transformerTag)? true : false
    });
  }
  onChipClick() {
    console.log('onChipClick');
    this.setState({ isSelectorVisible: true, isChipVisible: false });
  }

  toggleTagsEditorDialog() {
    console.log('toggleTagsEditorDialog');
    this.setState({
      cellMetadataEditorDialog: !this.state.cellMetadataEditorDialog,
    });
  }

  render() {
    const cellType = RESERVED_CELL_NAMES.includes(this.state.transformerTag)
      ? this.state.transformerTag : 'na';
    const cellColor = 'transparent';

    const prevStepNotice = this.getPrevStepNotice();

    return (
      <React.Fragment>
        <div
          className={ 'transformer-inline-cell-metadata' + (this.state.isChipVisible ? '' : ' hidden') }
        >
          <Tooltip
            placement="top"
            key={this.state.transformerTag + 'tooltip'}
            title={
              RESERVED_CELL_NAMES.includes(this.state.transformerTag)?
              RESERVED_CELL_NAMES_HELP_TEXT[this.state.transformerTag] :
              'This cell starts the pipeline step: ' + this.state.transformerTag
            }
          >
            <Chip
              className={ 'transformer-meta-chip' }
              key={ this.state.transformerTag }
              label={ this.state.transformerTag }
              onClick={() => this.onChipClick()}
            />
          </Tooltip>
        </div>
        <div
          className={ 'transformer-metadata-editor-wrapper' + (this.state.isSelectorVisible ? '' : ' hidden') }
        >
          <div
            className={ 'transformer-cell-metadata-editor' }
            style={{ borderLeft: `2px solid ${cellColor}` }}
          >
            <Select
              updateValue={this.updateCurrentCellTag}
              values={CELL_TYPE_SELECT_OPTIONS}
              value={cellType}
              label={'Cell type'}
              index={0}
              variant="outlined"
              style={{ width: 'auto', minWidth: '14em' }}
            />
            <IconButton
              aria-label="hide"
              onClick={() => this.hideSelector()}
            >
              <CloseIcon fontSize="small" />
            </IconButton>
            <IconButton
              className={ 'transformer-cell-metadata-editor-toggle' }
              aria-label="toggle"
              onClick={() => this.toggleSelector()}
              style={{ width: '0', height: '0', padding: '0' }}
            />
          </div>
          <div
            className={ 'transformer-cell-metadata-editor-helper-text' + (this.state.isSelectorVisible ? '' : ' hidden') }
          >
            <p>{prevStepNotice}</p>
          </div>
        </div>
      </React.Fragment>
    );
  }
}
