#!python3
import pandas as pd
import warnings

warnings.resetwarnings()
warnings.simplefilter("ignore", pd.errors.SettingWithCopyWarning)

df = pd.read_csv("./passwords.csv")
newPassData = df[["username", "password", "url", "httpRealm"]]
newPassData.insert(
    0,
    "formActionOrigin",
    df["formActionOrigin"].str.replace("http://", "").str.replace("https://", ""),
)
newPassData["timeCreated"] = pd.to_datetime(df["timeCreated"], unit="ms").dt.strftime(
    "%Y/%m/%d %H:%M:%S"
)
newPassData["timePasswordChanged"] = pd.to_datetime(
    df["timePasswordChanged"], unit="ms"
).dt.strftime("%Y/%m/%d %H:%M:%S")
newPassData.to_csv("./pass.csv", index=False, header=False)
