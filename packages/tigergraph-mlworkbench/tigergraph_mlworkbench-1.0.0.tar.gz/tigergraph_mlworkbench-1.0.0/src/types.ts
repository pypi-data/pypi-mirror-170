import { JupyterFrontEnd } from '@jupyterlab/application';
import { ISettingRegistry } from '@jupyterlab/settingregistry';

export type EmptyType = Record<string, never>;

export type ServerType = {
  serverName: string;
  serverAddress: string;
  hostOS: string;
  restPort: string;
  gsqlPort: string;
};

export type ServerDetailProps = ServerType & {
  submitServerDetail: (arg0: ServerType) => void;
  setEditingState: (arg0: boolean) => void;
};

export type ServerControllerState = {
  renderView: string;
};

export type ServerControllerProps = ServerType & {
  jupyterApp: JupyterFrontEnd;
  id: number;
  updateServer: (index: number, newServer: ServerType) => void;
  deleteServer: (idnex: number) => void;
};

export type ServerIndexState = {
  isAdding: boolean;
  serverList: Array<ServerType>;
};

export type ServerIndexProps = {
  jupyterApp: JupyterFrontEnd;
  settings: ISettingRegistry.ISettings;
};

export type DBControllerState = {
  renderComponent: string;
};

export type DBControllerProps = {
  serverAddress: string;
  hostOS: string;
  restPort: string;
  gsqlPort: string;
  jupyterApp: JupyterFrontEnd;
  handleExit: () => void;
};

export type DBInstallerState = {
  renderView: string;
  isLocalInstall: boolean;
  sshUsername: string;
  sshKeyfile: string;
};

export type DBInstallerProps = {
  serverAddress: string;
  hostOS: string;
  jupyterApp: JupyterFrontEnd;
  handleExit: () => void;
};

export type TmpOutputFormProps = {
  update: (state: {
    local_output_path: string;
    tg_output_path: string;
  }) => void;
};

export type SSHFormProps = {
  update: (state: {
    sshUsername: string;
    sshKeyfile: string;
    dbuser: string;
  }) => void;
};

export type VolumeMountFormProps = {
  update: (state: {
    local_output_path: string;
    tg_output_path: string;
  }) => void;
};
