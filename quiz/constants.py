from loan.choices import LoanRepaymentStatus
from nach.choices import (
    DebitPullRequestChoices,
    TrxnDocType,
)

CREDY_NACH_ID = 'NACH00000000005991'

DUE_LIMIT_SOFT = 4
DUE_LIMIT_HARD = 8

DR_HEADER_LAN_NO = 'Lan No'
DR_HEADER_UMRN = 'UMRN'
DR_HEADER_AMOUNT = 'Amount'
DR_HEADER_SETTLEMENT_DATE = 'Settlement Date'
DR_HEADER_USER_NUMBER = 'User Number'

DR_HEADER_LIST = [
    DR_HEADER_LAN_NO,
    DR_HEADER_UMRN,
    DR_HEADER_AMOUNT,
    DR_HEADER_SETTLEMENT_DATE,
    DR_HEADER_USER_NUMBER
]

DIR_NACH_FILE = 'nach_files'
SUB_DIR_DEBIT_REQUEST = 'debit_request'

FILE_PATH_MAP = {
    TrxnDocType.NACH_MANDATE.value: 'nach_mandate',
    TrxnDocType.DEBIT_REQUEST_CSV.value: 'debit_request'
}

DEBIT_PULL_FILE_NAME_FORMAT = ('NACH_DR_{}_NACH00000000005991_'
                               'CREADYTECHNOLOGIESPVTLTD_001')

NACH_PULL_EMAIL_MSG = ('Please check the attached file for the '
                       'pull requests to be made on {}')

LR_DR_STATUS_MAP = {
    LoanRepaymentStatus.DUE: DebitPullRequestChoices.DUE,
    LoanRepaymentStatus.PAID: DebitPullRequestChoices.PAID,
    LoanRepaymentStatus.DEFERRED: DebitPullRequestChoices.DEFERRED,
    LoanRepaymentStatus.LATE: DebitPullRequestChoices.LATE,
    LoanRepaymentStatus.PREPAID: DebitPullRequestChoices.PREPAID,
    LoanRepaymentStatus.PART_PAID: DebitPullRequestChoices.PART_PAID
}

MSG_MISSING_ATTACHMENT = 'Could not see file/attachment.'

EMAIL_SBJT_NACH_MANDATE_RESPONSE = (
    'Confidential | Status of NACH Registrations - NACH00000000005991 - '
    'CREADY TECHNOLOGIES PVT LTD'
)
EMAIL_SUBJECT_UMRN_UPDATE_FAILED = 'NACH UMRN update failed'
EMAIL_SUBJECT_NACH_REMINDER = 'Auto-Debit of your EMI tomorrow - {}'
EMAIL_SUBJECT_NACH_PLACED = ('Auto-Debit of Your Credy EMI '
                             'has been submitted - {}')
EMAIL_SUBJECT_DEBIT_PULL_ON_DATE = 'Debit Pull List for {}'

TEMPLATE_ADMIN_CSV_GENERATOR = 'admin/nach/nach_csv_generator.html'
TEMPLATE_EMAIL_UMRN_UPDATE_FAILED = 'emails/nach/umrn_update_failed.html'
TEMPLATE_EMAIL_NACH_REMINDER = 'emails/nach/nach_debit_notification.html'
TEMPLATE_EMAIL_NACH_PLACED = 'emails/nach/nach_pull_placed.html'
TEMPLATE_EMAIL_NACH_UPD_FAILED = 'emails/nach/umrn_update_failed.html'
TEMPLATE_MSG_NACH_REMINDER = 'sms/nach/nach_debit_notification.txt'
TEMPLATE_MSG_NACH_PLACED = 'sms/nach/nach_pull_placed.txt'


TASK_AGG_REPAYMENTS_TO_DEBITS = 'agg_loan_repayments_to_debit_pull'
TASK_SEND_EMAIL_NACH_FAILED_ACC = 'send-email-nach-failed-acc'
TASK_EXECUTE_NACH_PULL_NOTIF = 'execute_nach_pull_notification'
TASK_SEND_NACH_PLACED_NOTIF = 'send-nach-placed-notif'
TASK_UPLOAD_FILE_TO_SERVER = 'upload_nach-debit_file_to_server'
TASK_RESET_UPDATED_STATUS = 'reset_modified_status_of_debit_request'
TASK_CHECK_STATUS_UPLOADED_FILE = 'check_status_of_uploaded_file_on_server'

NACH_DEBIT_FILE_NAME = (
    'NACH_DR_{pull_date}_{nach_id}_{client_name}_{suffix}.csv')

MARK_NACH_DEBIT_FILE_NAME = 'MARK_DEBIT_NACH_{}'
