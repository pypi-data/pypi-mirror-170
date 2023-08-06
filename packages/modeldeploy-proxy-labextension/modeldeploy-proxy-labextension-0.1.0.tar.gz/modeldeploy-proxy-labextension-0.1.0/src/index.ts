import { JupyterFrontEndPlugin } from '@jupyterlab/application';
import TransformerCellSidebarPlugin from './sidebar';
import TransformerLeftPanelPlugin from './leftpanel';

export default [ TransformerCellSidebarPlugin, TransformerLeftPanelPlugin ] as JupyterFrontEndPlugin<any>[];
