from datetime import datetime
import json


def generate_etf_data():
  data = {
      "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      "etfs": [
          {
              "code": "00981A",
              "name": "統一台股增長主動式ETF",
              "category": "主動式ETF",
              "ytd": 18.5,
              "return_1y": 26.4,
              "return_2y": 48.2,
              "scale": 68.5,
              "price": 28.5,
              "change": 0.35,
              "holdings_change": [
                  {
                      "stock": "2330 台積電",
                      "action": "加碼",
                      "shares": "+50,000股",
                      "days": "連續3天加碼",
                  },
                  {
                      "stock": "2454 聯發科",
                      "action": "減碼",
                      "shares": "-20,000股",
                      "days": "連續2天減碼",
                  },
              ],
          },
          {
              "code": "00992A",
              "name": "群益台灣強棒主動式ETF",
              "category": "主動式ETF",
              "ytd": 21.2,
              "return_1y": 31.0,
              "return_2y": 55.6,
              "scale": 85.2,
              "price": 31.2,
              "change": 0.50,
              "holdings_change": [
                  {
                      "stock": "2317 鴻海",
                      "action": "加碼",
                      "shares": "+150,000股",
                      "days": "連續4天加碼",
                  }
              ],
          },
          {
              "code": "00991A",
              "name": "野村臺灣智慧優選主動ETF",
              "category": "主動式ETF",
              "ytd": 16.8,
              "return_1y": 24.5,
              "return_2y": 42.1,
              "scale": 45.0,
              "price": 24.8,
              "change": -0.15,
              "holdings_change": [],
          },
          {
              "code": "00994A",
              "name": "富邦台灣優勢動能主動ETF",
              "category": "主動式ETF",
              "ytd": 19.4,
              "return_1y": 28.9,
              "return_2y": 50.3,
              "scale": 52.3,
              "price": 27.1,
              "change": 0.20,
              "holdings_change": [],
          },
          {
              "code": "00980A",
              "name": "元大台灣卓越創新主動ETF",
              "category": "主動式ETF",
              "ytd": 15.2,
              "return_1y": 22.1,
              "return_2y": 39.8,
              "scale": 38.4,
              "price": 22.5,
              "change": 0.10,
              "holdings_change": [],
          },
          {
              "code": "0050",
              "name": "元大台灣50",
              "category": "市值型ETF",
              "ytd": 16.2,
              "return_1y": 24.1,
              "return_2y": 45.0,
              "scale": 3200.0,
              "price": 185.0,
              "change": 1.20,
              "holdings_change": [],
          },
          {
              "code": "00631L",
              "name": "元大台灣50正2",
              "category": "槓桿型ETF",
              "ytd": 38.2,
              "return_1y": 55.0,
              "return_2y": 95.0,
              "scale": 150.2,
              "price": 142.0,
              "change": 2.80,
              "holdings_change": [],
          },
          {
              "code": "00685L",
              "name": "群益臺灣加權正2",
              "category": "槓桿型ETF",
              "ytd": 36.5,
              "return_1y": 52.8,
              "return_2y": 91.0,
              "scale": 45.6,
              "price": 88.5,
              "change": 1.90,
              "holdings_change": [],
          },
          {
              "code": "00675L",
              "name": "富邦臺灣加權正2",
              "category": "槓桿型ETF",
              "ytd": 37.0,
              "return_1y": 53.5,
              "return_2y": 92.2,
              "scale": 62.1,
              "price": 95.0,
              "change": 2.10,
              "holdings_change": [],
          },
          {
              "code": "00663L",
              "name": "國泰臺灣加權正2",
              "category": "槓桿型ETF",
              "ytd": 36.8,
              "return_1y": 53.0,
              "return_2y": 91.5,
              "scale": 50.4,
              "price": 90.2,
              "change": 2.00,
              "holdings_change": [],
          },
      ],
  }

  with open("etf_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
  print("資料更新成功！")


if __name__ == "__main__":
  generate_etf_data()
