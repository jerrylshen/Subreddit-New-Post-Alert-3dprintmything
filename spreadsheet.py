import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Spreadsheet:
	def __init__(self, post_code):
		self.post_code = post_code
		self.replied = True
		self.cell = None
		self.row_count = 0
		self.sheet = None


	def accessDriveAPI(self):
		# use creds to create a client to interact with the Google Drive API
		scope = ['https://spreadsheets.google.com/feeds',
		         'https://www.googleapis.com/auth/drive']
		creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
		client = gspread.authorize(creds)

		# Find a workbook by name and open the first sheet
		# Make sure you use the right name here.
		self.sheet = client.open("r/3dprintmything").sheet1

		# Extract and print all of the values
		#list_of_hashes = self.sheet.get_all_records()
		#print(list_of_hashes)

	def getRows(self):
		self.row_count = self.sheet.row_count

	def checkIfPostRepliedTo(self):
		try:
			self.cell = self.sheet.find(self.post_code)

		except:
			self.replied = False


	def updateSheet(self):
		if not self.replied:
			self.sheet.add_rows(1)
			self.sheet.update_cell(self.row_count+1, 1, self.post_code)
			print(self.replied)
			print("post code:" + self.post_code)


	def run(self):
		self.accessDriveAPI()
		self.getRows()
		self.checkIfPostRepliedTo()
		self.updateSheet()
		return self.replied

