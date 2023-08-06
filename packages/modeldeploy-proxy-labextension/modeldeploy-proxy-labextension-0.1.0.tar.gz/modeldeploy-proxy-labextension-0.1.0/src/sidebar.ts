import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { IToolbarWidgetRegistry, createToolbarFactory } from '@jupyterlab/apputils';
import { ISettingRegistry } from '@jupyterlab/settingregistry';
import { ITranslator, nullTranslator } from '@jupyterlab/translation';
import { CellBarExtension } from '@jupyterlab/cell-toolbar';
import { treeViewIcon } from '@jupyterlab/ui-components';
import { INotebookTracker } from '@jupyterlab/notebook';

const sidebar_id = 'modeldeploy-proxy-labextension:sidebar';

export default {
    id: sidebar_id,
    requires: [INotebookTracker],
    autoStart: true,
    activate: async (
        app: JupyterFrontEnd,
        tracker: INotebookTracker,
        settingRegistry: ISettingRegistry | null,
        toolbarRegistry: IToolbarWidgetRegistry | null,
        translator: ITranslator | null
    ) => {
        console.log('Sidebar is now activating...');
        app.commands.addCommand('notebook:transformer', {
            label: 'Transformer',
            caption: 'Enable/disable transformer annotation widgets.',
            execute: args => {
                let currentCellIndex: number = tracker.currentWidget.content.activeCellIndex;
                let toggle: HTMLElement = (<Element>tracker.currentWidget.content.node.childNodes[currentCellIndex]).querySelector('.transformer-cell-metadata-editor-toggle') as HTMLElement;
                toggle.click();
            },
            icon: args => (args.toolbar ? treeViewIcon : ''),
            isEnabled: () => true,
            isVisible: () => true
        });
        const toolbarItems = settingRegistry && toolbarRegistry ? createToolbarFactory(
            toolbarRegistry,
            settingRegistry,
            CellBarExtension.FACTORY_NAME, // "Cell"
            sidebar_id,
            translator ?? nullTranslator
        ) : undefined;

        app.docRegistry.addWidgetExtension(
            'Notebook',
            new CellBarExtension(app.commands, toolbarItems)
        );
    },
    optional: [ISettingRegistry, IToolbarWidgetRegistry, ITranslator]
} as JupyterFrontEndPlugin<void>;
