[Setup]
AppId={{F7A3B8C2-9D4E-4F1A-8B3C-1D2E3F4A5B6C}
AppName=MisTareas 2.0
AppVersion=2.1
AppPublisher=Juan Fabián Viera Rosales
AppPublisherURL=https://github.com/Fabianviera/MisTareas2.0
DefaultDirName={autopf}\MisTareas2.0
DefaultGroupName=MisTareas 2.0
OutputDir=installer
OutputBaseFilename=Installer_MisTareas2.1
SetupIconFile=icon.ico
UninstallDisplayIcon={app}\MisTareas2.1.exe
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
Source: "dist\MisTareas2.1.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\MisTareas 2.0";             Filename: "{app}\MisTareas2.1.exe"; IconFilename: "{app}\MisTareas2.1.exe"
Name: "{group}\Desinstalar MisTareas 2.0"; Filename: "{uninstallexe}"
Name: "{autodesktop}\MisTareas 2.0";       Filename: "{app}\MisTareas2.1.exe"; IconFilename: "{app}\MisTareas2.1.exe"; Tasks: desktopicon
Name: "{userstartmenu}\MisTareas 2.0";     Filename: "{app}\MisTareas2.1.exe"; IconFilename: "{app}\MisTareas2.1.exe"

[Run]
Filename: "{app}\MisTareas2.1.exe"; Description: "Abrir MisTareas 2.0 ahora"; Flags: nowait postinstall skipifsilent

[Code]

{ Devuelve la cadena de desinstalación del registro, o vacía si no hay instalación previa }
function ObtenerCadenaDesinstalacion(): String;
var
  sRuta: String;
  sValor: String;
begin
  sRuta := 'Software\Microsoft\Windows\CurrentVersion\Uninstall\{F7A3B8C2-9D4E-4F1A-8B3C-1D2E3F4A5B6C}_is1';
  sValor := '';
  if not RegQueryStringValue(HKLM, sRuta, 'UninstallString', sValor) then
    RegQueryStringValue(HKCU, sRuta, 'UninstallString', sValor);
  Result := sValor;
end;

function InitializeSetup(): Boolean;
var
  sCadena: String;
  iResultado: Integer;
  iOpcion: Integer;
  aEtiquetas: TArrayOfString;
begin
  Result := True;
  sCadena := ObtenerCadenaDesinstalacion();

  if sCadena = '' then
    Exit; { No hay instalación previa — continuar normalmente }

  { Mostrar diálogo con tres opciones }
  SetArrayLength(aEtiquetas, 3);
  aEtiquetas[0] := 'Actualizar';
  aEtiquetas[1] := 'Eliminar aplicación';
  aEtiquetas[2] := 'Cancelar';

  iOpcion := TaskDialogMsgBox(
    'MisTareas ya está instalado',
    'Se ha detectado una versión anterior de MisTareas en este equipo.' + #13#10 +
    '¿Qué deseas hacer?',
    mbConfirmation,
    MB_YESNOCANCEL,
    aEtiquetas,
    0
  );

  if iOpcion = IDYES then
  begin
    { Actualizar: desinstalar en silencio y continuar con la instalación }
    Exec(RemoveQuotes(sCadena), '/SILENT', '', SW_HIDE, ewWaitUntilTerminated, iResultado);
    Result := True;
  end
  else if iOpcion = IDNO then
  begin
    { Eliminar: desinstalar y salir }
    if MsgBox(
      '¿Confirmas que quieres eliminar MisTareas del equipo?',
      mbConfirmation, MB_YESNO
    ) = IDYES then
      Exec(RemoveQuotes(sCadena), '/SILENT', '', SW_HIDE, ewWaitUntilTerminated, iResultado);
    Result := False;
  end
  else
  begin
    { Cancelar: salir sin hacer nada }
    Result := False;
  end;
end;
