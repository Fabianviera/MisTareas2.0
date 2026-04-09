[Setup]
AppName=MisTareas 2.0
AppVersion=2.1
AppPublisher=Juan Fabián Viera Rosales
AppPublisherURL=https://github.com/Fabianviera/MisTareas2.0
DefaultDirName={autopf}\MisTareas2.0
DefaultGroupName=MisTareas 2.0
OutputDir=installer
OutputBaseFilename=Installer_MisTareas2.0
SetupIconFile=icon.ico
UninstallDisplayIcon={app}\MisTareas2.0.exe
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
AllowNoIcons=no

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "Crear acceso directo en el Escritorio"; GroupDescription: "Accesos directos:"

[Files]
Source: "dist\MisTareas2.0.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\MisTareas 2.0";             Filename: "{app}\MisTareas2.0.exe"; IconFilename: "{app}\MisTareas2.0.exe"
Name: "{group}\Desinstalar MisTareas 2.0"; Filename: "{uninstallexe}"
Name: "{autodesktop}\MisTareas 2.0";       Filename: "{app}\MisTareas2.0.exe"; IconFilename: "{app}\MisTareas2.0.exe"; Tasks: desktopicon
Name: "{userstartmenu}\MisTareas 2.0";     Filename: "{app}\MisTareas2.0.exe"; IconFilename: "{app}\MisTareas2.0.exe"

[Run]
Filename: "{app}\MisTareas2.0.exe"; Description: "Abrir MisTareas 2.0 ahora"; Flags: nowait postinstall skipifsilent
