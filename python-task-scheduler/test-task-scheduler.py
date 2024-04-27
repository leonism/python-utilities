import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import task_scheduler

class TestTaskScheduler(unittest.TestCase):

    @patch('task_scheduler.subprocess')
    def test_check_dependencies(self, mock_subprocess):
        with patch('builtins.print') as mocked_print:
            task_scheduler.check_dependencies()
            mocked_print.assert_called_with("colorama module found.")
            mock_subprocess.run.assert_not_called()

        mock_subprocess.reset_mock()

        # Test case where colorama module is not found
        mock_subprocess.run.side_effect = Exception()
        with patch('builtins.print') as mocked_print:
            task_scheduler.check_dependencies()
            mocked_print.assert_called_with("colorama module not found. Installing...")
            mock_subprocess.run.assert_called_once()

    @patch('task_scheduler.smtplib.SMTP_SSL')
    def test_send_email(self, mock_smtp):
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_smtp_instance
        task_scheduler.send_email("Test Subject", "Test Message")
        mock_smtp_instance.login.assert_called_once()
        mock_smtp_instance.send_message.assert_called_once()

    def test_backup_task(self):
        with patch('task_scheduler.print') as mocked_print:
            task_scheduler.backup_task()
            mocked_print.assert_called_with(task_scheduler.Fore.GREEN + "Running backup task..." + task_scheduler.Style.RESET_ALL)

    def test_transfer_task(self):
        with patch('task_scheduler.print') as mocked_print:
            task_scheduler.transfer_task()
            mocked_print.assert_called_with(task_scheduler.Fore.GREEN + "Running transfer task..." + task_scheduler.Style.RESET_ALL)

    def test_sync_task(self):
        with patch('task_scheduler.print') as mocked_print:
            task_scheduler.sync_task()
            mocked_print.assert_called_with(task_scheduler.Fore.GREEN + "Running synchronization task..." + task_scheduler.Style.RESET_ALL)

if __name__ == '__main__':
    unittest.main()
