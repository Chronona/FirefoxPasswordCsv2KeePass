# FirefoxPasswordCsv4KeePass

## なにこれ
Firefoxが生成するpasswords.csvを、KeePassへのインポート用へ整形するPythonスクリプト。  
FireFoxとKeePassとの連携が失敗する、あるいはプラグインを入れたくない人向け。

passwords.csvをそのままインポートすると、列順の編集やUnix epoch timeの変換が必要になる。  
操作が面倒なので、その手間を省くスクリプトを作成した。

## 必要なもの（カッコ内のバージョンで動作確認済み）
- Python3 (3.10.11)
  - Panads (2.2.0)
- Firefox (128.0.3)
- KeePass (2.57)

## 使い方

### 準備

1. Code>Download Zipを選択
2. ファイルを解凍（FirefoxPasswordCsv4KeePass-mainフォルダが生成される）
3. pipインストール（pandasインストール済なら無視）
   ```python
   pip install -r requirements.txt
   ```

### FireFoxからパスワードファイルをダウンロード
1. Firefoxのメニューにある「パスワード」を選択
2. 右上の"..."をクリックして「パスワードをエクスポート」を選択  
   
   ![firefox](https://github.com/user-attachments/assets/d45f8e0e-b17e-49f9-91fa-2dea5ab5e120)
4. password.csvをFirefoxPasswordCsv4KeePass-main内に保存

### 実行
1. main.pyをダブルクリックして実行
2. pass.csvが生成されれば成功

### KeePassへインポート
1. KeePassのメニューから「ファイル>インポート」を選択
2. 「一般的なCSVインポーター」（Generic CSV Importer）を選択
3. ファイル入力欄には、生成したpass.csvを選択
4. （任意：パスワード作成日時が不要な場合は次へ）  
   構造タブでフィールドを追加  
   - 型：作成日時, 書式:yyyy/MM/dd HH:mm:ss
   - 型：最終更新日時, 書式:yyyy/MM/dd HH:mm:ss
   ![columns](https://github.com/user-attachments/assets/4195469c-9708-4884-b12d-3fa8ac64d845)
6. プレビュータブを押して、問題なければ「完了」を選択

