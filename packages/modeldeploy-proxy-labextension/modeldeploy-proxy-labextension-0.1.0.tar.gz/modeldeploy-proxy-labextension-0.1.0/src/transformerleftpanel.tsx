import * as React from 'react';
import { INotebookTracker, NotebookPanel } from '@jupyterlab/notebook';
import { JupyterFrontEnd } from '@jupyterlab/application';
import { IDocumentManager } from '@jupyterlab/docmanager';
import { ThemeProvider } from '@material-ui/core/styles';
import { theme } from './theme';
import { Button } from '@material-ui/core';
import { InlineCellsMetadata } from './widgets/InlineCellsMetadata';
import { PageConfig } from '@jupyterlab/coreutils';
import { executeRpc, globalUnhandledRejection } from './lib/RPCUtils';
import NotebookUtils from './lib/NotebookUtils';
import { Kernel } from '@jupyterlab/services';

interface IProps {
  app: JupyterFrontEnd;
  tracker: INotebookTracker;
  docManager: IDocumentManager;
}

interface IState {
  runDeployment: boolean;
  deploymentType: string;
  deployDebugMessage: boolean;
  notebookVolumes?: IVolumeMetadata[];
  volumes?: IVolumeMetadata[];
  isEnabled: boolean;
  namespace: string;
}

export interface IVolumeMetadata {
  type: string;
  name: string;
  mount_point: string;
  size?: number;
  size_type?: string;
  snapshot: boolean;
  snapshot_name?: string;
}

export const DefaultState: IState = {
  runDeployment: false,
  deploymentType: 'compile',
  deployDebugMessage: false,
  notebookVolumes: [],
  volumes: [],
  isEnabled: false,
  namespace: '',
};

export class TransformerLeftPanel extends React.Component<IProps, IState> {
    state = DefaultState;

    getActiveNotebookPanel = () => {
        return this.props.tracker.currentWidget;
    };

    getActiveNotebookPath = () => {
        return (this.getActiveNotebookPanel() && PageConfig.getOption('serverRoot') + '/' + this.getActiveNotebookPanel().context.path);
    };

  getNotebookMountPoints = (): { label: string; value: string }[] => {
    const mountPoints: { label: string; value: string }[] = [];
    return mountPoints;
  };

  activateRunDeployState = (type: string) => {
  };

  updateVolumes = (
    volumes: IVolumeMetadata[],
    metadataVolumes: IVolumeMetadata[],
  ) => {
  };

  // restore state to default values
  resetState = () =>
    this.setState((prevState, props) => ({
      ...DefaultState,
      isEnabled: prevState.isEnabled,
    }));

  componentDidMount = () => {
    // Notebook tracker will signal when a notebook is changed

    // Set notebook widget if one is open
    if (this.props.tracker.currentWidget instanceof NotebookPanel) {
    }
  };

  componentDidUpdate = (
    prevProps: Readonly<IProps>,
    prevState: Readonly<IState>,
  ) => {
  };

  /**
   * This handles when a notebook is switched to another notebook.
   * The parameters are automatically passed from the signal when a switch occurs.
   */
  handleNotebookChanged = async (
    tracker: INotebookTracker,
    notebook: NotebookPanel,
  ) => {
  };

  /**
   * Read new notebook and assign its metadata to the state.
   * @param notebook active NotebookPanel
   */
  setNotebookPanel = async (notebook: NotebookPanel) => {
  };

  onPanelRemove = (index: number) => {
  };

  runDeploymentCommand = async () => {
  };

    applyTransformerToProxy = async () => {
        console.log('applyTransformerToProxy');

        await NotebookUtils.saveNotebook(this.getActiveNotebookPanel(), true, true);
        if (! this.getActiveNotebookPanel().context.model.dirty) {
            //  this.setState({ katibDialog: true });
        }
        console.log(this.getActiveNotebookPath());
        try {
            const kernel: Kernel.IKernelConnection = await NotebookUtils.createNewKernel();
            await executeRpc(kernel, 'log.setup_logging');
            const args = {
                source_notebook_path: this.getActiveNotebookPath()
            }
            const result = await executeRpc(kernel, 'nb.parse_notebook', args);
            console.log(result);
        } catch (error) {
            globalUnhandledRejection({ reason: error });
            throw error;
        }
  };

  onMetadataEnable = (isEnabled: boolean) => {
    this.setState({ isEnabled });
  };

  render() {
    return (
      <ThemeProvider theme={theme}>
        <div className={'leftpanel-transformer-widget'} key="transformer-widget">
          <div className={'leftpanel-transformer-widget-content'}>
            <div>
              <p
                style={{
                  fontSize: 'var(--jp-ui-font-size3)'
                }}
                className="kale-header"
              >
                Transformer Panel {this.state.isEnabled}
              </p>
            </div>

            <div className="cells-meta-component">
              <InlineCellsMetadata
                onMetadataEnable={this.onMetadataEnable}
                notebookPanel={this.getActiveNotebookPanel()}
              />
            </div>

            <div
              className={
                'kale-component ' + (this.state.isEnabled ? '' : 'hidden')
              }
            >
              <div>
                <p
                  className="kale-header"
                  style={{ color: theme.transformer.headers.main }}
                >
                  Transformer is the plugin for pre-processor / post-preocessor...
                </p>
              </div>
            </div>

            <div
              className={
                'kale-component ' + (this.state.isEnabled ? '' : 'hidden')
              }
            >
              <div>
                <p
                  className="transformer-header"
                  style={{ color: theme.transformer.headers.main }}
                >
                  Run
                </p>
              </div>
              <div className="input-container add-button">
                <Button
                  variant="contained"
                  color="primary"
                  size="small"
                  title="SetupKatibJob"
                  onClick={this.applyTransformerToProxy}
                  disabled={ false }
                  style={{ marginLeft: '10px', marginTop: '0px' }}
                >
                  Apply Changes
                </Button>
              </div>
            </div>

            <div
              className={
                'kale-component ' + (this.state.isEnabled ? '' : 'hidden')
              }
            >
            </div>
          </div>
          <div
            className={this.state.isEnabled ? '' : 'hidden'}
            style={{ marginTop: 'auto' }}
          >
          </div>
        </div>
      </ThemeProvider>
    );
  }
}
